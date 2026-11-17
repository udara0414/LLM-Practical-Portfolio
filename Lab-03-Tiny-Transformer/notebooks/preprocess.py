from datasets import load_dataset
from itertools import islice

# Load a small subset of TinyStories
dataset = load_dataset(
    "roneneldan/TinyStories",
    split="train",
    streaming=True
)

# Select 1000 stories
stories = list(islice(dataset, 1000))

# Combine all stories into one text
text = "\n".join(story["text"] for story in stories)

# Create character vocabulary
chars = sorted(list(set(text)))

# Create character-to-integer mapping
stoi = {ch: i for i, ch in enumerate(chars)}

# Create integer-to-character mapping
itos = {i: ch for ch, i in stoi.items()}

# Encode text into numbers
encoded_text = [stoi[ch] for ch in text]

# Decode numbers back into text
decoded_text = "".join(itos[i] for i in encoded_text)

# Display results
print("Text preprocessing completed!")
print("Number of stories:", len(stories))
print("Total characters:", len(text))
print("Vocabulary size:", len(chars))

print("\nOriginal text:")
print(text[:200])

print("\nEncoded text:")
print(encoded_text[:50])

print("\nDecoded text:")
print(decoded_text[:200])