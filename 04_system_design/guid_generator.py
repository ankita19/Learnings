import uuid

# Generate 10 GUIDs (UUID v4)
guids = [str(uuid.uuid4()) for _ in range(10)]

for g in guids:
    print(g)