import torch
import math

from model import TinyTransformer


# 1. Select device
device = "cuda" if torch.cuda.is_available() else "cpu"


# 2. Load prepared data
checkpoint = torch.load(
    "training_data.pt",
    map_location="cpu",
    weights_only=False
)

train_data = checkpoint["train_data"]
val_data = checkpoint["val_data"]


# 3. Load trained model
model = TinyTransformer().to(device)

model.load_state_dict(
    torch.load(
        "trained_model.pth",
        map_location=device,
        weights_only=True
    )
)

model.eval()

print("Trained model loaded successfully!")


# 4. Evaluate model
@torch.no_grad()
def evaluate(data, batch_size=16, eval_iters=20):

    losses = []

    block_size = checkpoint["block_size"]

    for _ in range(eval_iters):

        ix = torch.randint(
            len(data) - block_size - 1,
            (batch_size,)
        )

        x = torch.stack([
            data[i:i + block_size] for i in ix
        ]).to(device)

        y = torch.stack([
            data[i + 1:i + block_size + 1] for i in ix
        ]).to(device)

        logits, loss = model(x, y)

        losses.append(loss.item())

    return sum(losses) / len(losses)


# 5. Calculate losses
train_loss = evaluate(train_data)
val_loss = evaluate(val_data)


# 6. Calculate perplexity
train_perplexity = math.exp(train_loss)
val_perplexity = math.exp(val_loss)


# 7. Display results
print("\nModel Evaluation Results")

print("Training Loss:", train_loss)
print("Validation Loss:", val_loss)

print("\nPerplexity Results")

print("Training Perplexity:", train_perplexity)
print("Validation Perplexity:", val_perplexity)