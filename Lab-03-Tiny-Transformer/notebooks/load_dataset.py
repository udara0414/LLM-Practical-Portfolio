from datasets import load_dataset
from itertools import islice

# Load TinyStories dataset
dataset = load_dataset(
    "roneneldan/TinyStories",
    split="train",
    streaming=True
)

# Select the first 10 stories
stories = list(islice(dataset, 10))

# Display dataset information
print("Dataset loaded successfully!")
print("Number of selected stories:", len(stories))

# Display sample stories
for i, story in enumerate(stories[:5], start=1):

    print(f"\nStory {i}")
    print("-" * 50)

    text = story["text"]

    print(text)
    print("Text length:", len(text), "characters")