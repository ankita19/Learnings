# Transformers — Simple Explanation

The intuition behind the architecture powering GPT/BERT, stripped of the scary math.
Connects directly to **contextual embeddings** (see the RAG / contextual-retrieval work in
this repo — same core idea).

---

## The one thing a Transformer does
> **Predict the next word.** ChatGPT is just this run in a loop: predict next word → add it →
> predict the next → repeat. Everything else is machinery to predict that next word *well*.

### Explain it to a 10-year-old
Imagine a game where you finish someone's sentence. To guess the next word, you read everything
they said and pay **extra attention to the words that matter most** — for *"a sweet Indian rice
___"* you focus on "sweet" and "Indian" and guess *kheer*, not *pizza*. A transformer plays this
exact game: it turns every word into numbers, lets each word peek at the other words and borrow
meaning from the important ones, then picks the most likely next word — and does it again and
again, one word at a time, until it's written a whole answer. That's all ChatGPT is: a really,
really good fill-in-the-blank game.

## The whole thing in 3 steps

```
   TEXT:  "I made sweet Indian rice ___"
    │     (a list of words)
    ▼
1. EMBEDDINGS   turn each word into a vector that captures meaning
    │     OUT: one meaning-vector per word
    ▼
2. ATTENTION    let each word absorb context from the relevant words
    │     OUT: one context-enriched vector per word
    ▼
3. PREDICT      use those vectors to score the whole vocabulary
    │     OUT: probabilities → pick the top word
    ▼
   NEXT WORD:  "dish"   (then loop: add it, predict again)
```

---

## Step 1 — Embeddings (words → meaningful numbers)
> **In:** the sentence as a list of words → `["I", "made", "sweet", "Indian", "rice", "dish"]`
> **Out:** one **meaning-vector** per word (a list of numbers — 768 for BERT, 12,288 for GPT)

Computers understand numbers, not words. Each word becomes a **vector**; similar meanings land
near each other and directions carry meaning:
- `King − man + woman ≈ Queen`

**Problem with static embeddings:** *"track"* means different things in *"train on the track"*
vs *"track my package."* A fixed vector can't capture both.

**Fix = contextual embeddings** (the same idea as contextual retrieval): a word's vector gets
adjusted by its surrounding words. *"dish"* differs in *"rice dish"* vs *"sweet Indian rice
dish."* **This is the heart of Transformers** — the rest is *how* it builds that context.

## Step 2 — Attention (how context gets added)
> **In:** one meaning-vector per word (from Step 1)
> **Out:** one **context-enriched** vector per word — same count, but each is now blended with
> the meaning of the words around it

**Start with how YOU read.** Take the word **"it"** in:
*"The dog didn't cross the road because **it** was too tired."*
To know what "it" means, your brain automatically looks back and lands on **"dog"**, not "road."
You *paid attention* to the right word. **That is the entire idea of attention.**

> **Attention = every word automatically looks at all the other words, and pulls in meaning from
> the ones that matter — ignoring the ones that don't.**

### A simple example
Building the meaning of **dish** in *"sweet Indian rice dish"*. How much does "dish" pay
attention to each other word?

| Other word | Attention from "dish" | Why |
|---|---|---|
| sweet | 🟩🟩🟩 high | changes the meaning → *kheer*, not biryani |
| Indian | 🟩🟩 high | sets the cuisine |
| rice | 🟩🟩 high | the base ingredient |
| made | ⬜ low | doesn't change *what* a dish is |
| I | ⬜ low | doesn't change *what* a dish is |

So "dish" becomes a **blend**: mostly itself, plus a big dose of *sweet / Indian / rice*. That
blend is its **contextual embedding**. Swap *sweet* → *spicy* and the blend shifts → now it
predicts *biryani*. That's attention doing its job.

**Everything below is just HOW the model decides those percentages.** The idea above is the
*what* — that's the part that actually matters. Read the rest only if you're curious about the
mechanism.

### Q / K / V — the professor analogy (the "how", made simple)

| Term | Plain meaning | Analogy |
|---|---|---|
| **Query (Q)** | "What am I looking for?" | Professor: *"I need help on quantum computing"* |
| **Key (K)** | "What does each word offer?" | Students: *"I know quantum mechanics" / "I know philosophy"* |
| **Value (V)** | "The actual content to take" | The paragraphs each student writes |

**Mechanics:** `Q · K = attention score` (how well they match). High match → take more of that
word's **Value**. Sum the weighted Values → the contextual embedding. (Professor takes 60% from
the quantum student, 1% from the philosophy student.)

### Where Q, K, V come from — the "three lenses" (this is the minute-35 part)
Each word's embedding is multiplied by **three learned matrices** — WQ, WK, WV — to produce its
Query, Key, and Value. Think of WQ/WK/WV as **three lenses** you put on the same word:

| Lens | Turns the word into… | Meaning |
|---|---|---|
| **WQ** | its **Query** | "what am I looking for?" |
| **WK** | its **Key** | "what do I offer?" |
| **WV** | its **Value** | "what content do I contribute?" |

Same word → three different views, made by three different lenses. **The lenses are just numbers
the model learns during training** (via backprop, like any neural-net weight) and are then fixed.
You never compute them by hand.

> ⚠️ **Don't panic at the matrix math.** The slide showing `64×768`, multiplying rows by columns,
> and summing is just *how* a matrix multiply works — it's mechanics, not a new idea. **Skip it.**
> The only thing to remember: *Q, K, V = embedding × three learned matrices.*

## Step 3 — Supporting machinery (don't get lost here)
> **In:** the context-enriched vectors from attention
> **Out:** even richer vectors → finally, after **Linear + Softmax**, a probability for every word
> in the vocabulary → pick the highest = the **next word**

These pieces wrap around Step 2 to make attention work better and to turn the final vectors into
an actual word:

| Piece | Why it exists (one line) |
|---|---|
| **Positional embedding** | Transformers read all words at once (parallel), so they add a "position tag" — order matters (*"I made dish"* ≠ *"dish made I"*) |
| **Multi-head attention** | Run attention many times in parallel — one head tracks adjectives, one verbs, one pronouns. Different relationships at once. |
| **Feed-forward network (FFN)** | Attention captures *relationships* (linear); FFN adds *non-linear* depth for nuance |
| **Nx / stacked layers** | Repeat the block 12–96 times — each layer enriches further |
| **Encoder vs Decoder** | **Encoder** builds contextual embeddings (BERT). **Decoder** predicts next word (GPT). |
| **Cross-attention (decoder)** | For translation: Query comes from the output sentence, Key/Value from the input sentence |

---

## Reading the official diagram ("Attention Is All You Need", 2017)

![Transformer architecture from "Attention Is All You Need"](TheTransformer-modelarchitecture.png)

**Two towers:** the **left = Encoder**, the **right = Decoder**. Read each from the
**bottom up**. The `Nx` means the gray block is **stacked N times** (e.g. 6 in the original
paper, 12–96 in real models).

### Left tower — Encoder (turns input into contextual embeddings)
Bottom → top:
1. **Inputs** → **Input Embedding** — words become vectors (Step 1).
2. **⊕ Positional Encoding** — the circle-with-sine-wave is the position signal; `⊕` means
   it's *added* to the embedding so the model knows word order.
3. **Multi-Head Attention** — the 3 arrows feeding in are **Q, K, V** (all from the input
   here = *self-attention*). Words absorb context from each other (Step 2).
4. **Add & Norm** — *Add* = residual connection (add the block's input back to its output, for
   smooth gradient flow); *Norm* = layer normalization (stabilizes training).
5. **Feed Forward** → **Add & Norm** — the non-linear enrichment (Step 3).
6. Repeat `Nx`. Output = context-rich embeddings, fed sideways into the decoder.

### Right tower — Decoder (generates the output, one word at a time)
Bottom → top:
1. **Outputs (shifted right)** → **Output Embedding** + **Positional Encoding** — the words
   generated *so far*. "Shifted right" = at each step it only sees previous words, so it's
   forced to predict the next one (this is also how it's trained — *teacher forcing*).
2. **Masked Multi-Head Attention** — same as self-attention, but **masked** so a word can only
   attend to *earlier* words, never peek at future ones (you can't use the answer to predict
   the answer).
3. **Add & Norm**.
4. **Multi-Head Attention (the middle one) = CROSS-ATTENTION** — the key block. Notice its
   arrows: **K and V come from the Encoder** (the long arrow from the left tower), **Q comes
   from the decoder**. This is where the output looks back at the input — e.g. while writing
   the Hindi translation, it attends to the English sentence.
5. **Add & Norm** → **Feed Forward** → **Add & Norm**.
6. Repeat `Nx`.

### Top — turning vectors into a word
1. **Linear** — projects the final vector to the size of the whole vocabulary (~30k–50k scores).
2. **Softmax** — turns those scores into probabilities (sum to 1).
3. **Output Probabilities** — pick the highest-probability word = the predicted next word.
   Feed it back into "Outputs (shifted right)" and repeat.

### Block cheat-sheet
| Block in diagram | Plain meaning |
|---|---|
| Input / Output Embedding | words → vectors |
| Positional Encoding (⊕ sine icon) | adds word-order info |
| Multi-Head Attention | self-attention: words share context (Q,K,V all from same sequence) |
| Masked Multi-Head Attention | decoder self-attention that can't see future words |
| Multi-Head Attention (middle of decoder) | **cross-attention**: Q from decoder, K/V from encoder |
| Add & Norm | residual connection + layer normalization |
| Feed Forward | non-linear enrichment |
| Nx | stack the block N times |
| Linear → Softmax | final vector → vocabulary probabilities → next word |

> **GPT vs BERT on this diagram:** **BERT = the left tower only** (encoder). **GPT = the right
> tower only** (decoder, with masked attention — that's why it generates left-to-right). The
> full two-tower diagram is the original *translation* model.

## How it learns (training)
Self-supervised: take huge text, hide the next word, guess it, measure error, backpropagate
over millions of sentences. That's how WQ/WK/WV and the FFN weights get learned. No human
labeling needed — the next word *is* the label.

---

## The mental model to keep
> A Transformer takes each word's rough meaning (embedding), lets every word **borrow context**
> from the relevant words around it (attention), does this from many angles (multi-head) and
> many times (layers), and uses the final context-rich vectors to **predict the next word.**

---

## Interview angle (likely for AI/ML roles)

**"Explain self-attention."**
> Each word builds a query of what context it needs; every word offers a key describing what it
> provides and a value with its content. Score query·key for relevance, then take a weighted sum
> of values. That's how 'dish' absorbs 'sweet' and 'Indian' to become context-aware.

**"Why Transformers over RNNs?"**
> RNNs process words sequentially — slow and they forget long-range context. Transformers
> process all words in parallel and let any word attend directly to any other, near or far.
> Parallelism + long-range context is why they scaled.

> You don't need the matrix math (WQ dims, softmax scaling) unless it's an ML-research role —
> the intuition above is what gets tested for engineering roles.

## Don't panic — what to skip vs. must-know
When the video gets heavy (especially ~min 33–42), here's what actually matters for an
engineering interview vs. what's just implementation plumbing.

| ✅ MUST-KNOW (the intuition) | ❌ SKIP (the plumbing) |
|---|---|
| Goal = predict the next word | The exact matrix dimensions (64×768, 12,288, etc.) |
| Embeddings capture meaning; static vs **contextual** | Multiplying rows × columns by hand |
| **Attention** = words borrow context from relevant words | The √dk softmax-scaling detail |
| **Q/K/V** via the professor analogy + "three lenses" | Tracing the arithmetic of one Q vector |
| Multi-head = many relationships at once | Sinusoidal positional-encoding formula |
| Encoder (BERT) vs Decoder (GPT); cross-attention bridges them | Layer-by-layer tensor shapes |

**Rule of thumb:** if it's a *formula or a dimension*, skip it. If it's a *what does this do
and why*, keep it. You already understood the part that matters (attention) at the professor
analogy — the math slides are just the gears turning underneath.

**30-second self-check:** *"Where do Q, K, V come from?"* →
*"Multiply each word's embedding by three learned matrices, WQ/WK/WV — learned lenses, training
figures them out."* If you can say that, you've got the hard part.

## See also
- Visualizer: poloclub.github.io/transformer-explainer
- 3Blue1Brown "Neural networks" series (videos on attention) — best visual deep-dive
- This repo: `rag_example/`, and `../reference/claude-cookbooks/.../contextual-embeddings/`
