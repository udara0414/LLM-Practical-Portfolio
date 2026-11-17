import torch
from datasets import load_dataset
from itertools import islice

# Load TinyStories dataset
dataset = load_dataset(
    "roneneldan/TinyStories",
    split="train",
    streaming=True
)

# Select 1000 stories
stories = list(islice(dataset, 1000))

# Combine stories
text = "\n".join(story["text"] for story in stories)

# Create vocabulary
chars = sorted(list(set(text)))

# Create mappings
stoi = {ch: i for i, ch in enumerate(chars)}
itos = {i: ch for ch, i in stoi.items()}

# Encode text
data = torch.tensor(
    [stoi[ch] for ch in text],
    dtype=torch.long
)

# Split into training and validation data
split_index = int(0.9 * len(data))

train_data = data[:split_index]
val_data = data[split_index:]

# Define sequence length
block_size = 64

# Function to create input and target batches
def get_batch(data, batch_size=4):

    ix = torch.randint(
        len(data) - block_size - 1,
        (batch_size,)
    )

    x = torch.stack([
        data[i:i + block_size] for i in ix
    ])

    y = torch.stack([
        data[i + 1:i + block_size + 1] for i in ix
    ])

    return x, y


# Create sample training batch
x, y = get_batch(train_data)

# Display results
print("Training data preparation completed!")

print("\nDataset information:")
print("Total characters:", len(data))
print("Training characters:", len(train_data))
print("Validation characters:", len(val_data))
print("Vocabulary size:", len(chars))

print("\nTraining batch:")
print("Input shape:", x.shape)
print("Target shape:", y.shape)

# Display sample sequences
print("\nInput sequence:")
print("".join(itos[i.item()] for i in x[0]))

print("\nTarget sequence:")
print("".join(itos[i.item()] for i in y[0]))

# Save prepared data
torch.save({
    "train_data": train_data,
    "val_data": val_data,
    "stoi": stoi,
    "itos": itos,
    "vocab_size": len(chars),
    "block_size": block_size
}, "training_data.pt")

print("\nTraining data saved successfully!")