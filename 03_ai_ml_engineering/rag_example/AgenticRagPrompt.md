flowchart TD
    A([👤 Support Agent\nasked a question in D365 UI]) --> B

    B[AgentAssist WebAPI\nASP.NET Core endpoint\nreceives the HTTP request]

    B --> C{Which mode\nis turned on?}

    C -->|Feature flag OFF\nDefault mode| D[V1 — Standard\nAgentic Loop]
    C -->|Feature flag ON\nExperiment| E[V2 — Orchestrator\nLoop with client\ncontinuation support]

    subgraph LOOP [🔁 Agentic Loop — runs up to 5 times]
        direction TB

        D --> F[Step 1: Prepare the prompt\n\nBuild a message history:\n- system instructions from AgenticRagPrompt.md\n- user question\n- any previous tool results]

        F --> G[Step 2: Call the LLM\n\nSend prompt to Azure OpenAI via CAPI\nStream the response back in real-time\n📡 Technology: Azure OpenAI GPT-4]

        G --> H{Step 3: What did\nthe LLM decide?}

        H -->|LLM said:\n'I need to search for info'| I[Tool Required\n\nRun up to 3 tools in parallel]

        H -->|LLM said:\n'I have enough info, answer now'| J[Final Action\n\nStop the loop,\nbuild the final answer]

        H -->|LLM said:\n'Delegate this to a sub-agent'| K[Handover Action\n\nSend to SubAgentService\nwhich runs its own mini loop]

        H -->|Something unexpected| L[Unhandled Action\nLog + fallback response]

        subgraph TOOLS [🛠 Available Tools — LLM picks which to call]
            I --> T1[knowledge_search\n\nSearch the KB / Dataverse\nfor articles matching the query\n📦 Uses: IKnowledgeGenerator\n→ vector + relevance scored chunks]
            I --> T2[document_search\n\nSearch internal documents\nSame knowledge pipeline]
            I --> T3[generate_answer\n\nAsk a separate sub-agent\nto synthesize an answer\nfrom gathered results\n🤖 Uses a different AI model]
        end

        T1 --> M[Tool Results\nappended to message history]
        T2 --> M
        T3 --> M
        M --> F
    end

    J --> N[PostProcessor\n\nFormat the final text\nAttach citations from\nknowledge search results]

    K --> SA[SubAgentService\n\nSame loop logic, but scoped\nto a focused sub-task\nUses GenerateAnswerService\nwith a dedicated model endpoint]
    SA --> N

    N --> O[CitationProcessor\n\nMatch each piece of text\nto its source document\nURL, title, relevance score]

    O --> P([📤 Stream the response\nback to D365 UI\n\nReal-time chunks via\nIAsyncEnumerable\nwith citations attached])

    subgraph LIMITS [⚙️ Safety Guardrails]
        L1[Max 3 iterations\n+ 2 buffer = 5 total]
        L2[Max 3 tools per iteration]
        L3[100 sec timeout\nV2: client resumes\nif near HTTP 120s limit]
    end