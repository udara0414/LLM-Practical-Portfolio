import torch
import torch.nn as nn
import csv

from model import TinyTransformer


# 1. Select device
device = "cuda" if torch.cuda.is_available() else "cpu"

print("Training device:", device)


# 2. Load prepared training data
checkpoint = torch.load(
    "training_data.pt",
    map_location="cpu",
    weights_only=False
)

train_data = checkpoint["train_data"]
val_data = checkpoint["val_data"]

print("Training data loaded successfully!")


# 3. Model configuration
vocab_size = checkpoint["vocab_size"]
block_size = checkpoint["block_size"]

batch_size = 16
learning_rate = 0.001
max_iters = 1000
eval_interval = 100
eval_iters = 20


# 4. Create Transformer model
model = TinyTransformer().to(device)

print("Transformer model initialized!")


# 5. Configure optimizer
optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=learning_rate
)


# 6. Function to create batches
def get_batch(data):

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

    return x.to(device), y.to(device)


# 7. Evaluate training and validation loss
@torch.no_grad()
def estimate_loss():

    model.eval()

    results = {}

    for split, data in [
        ("train", train_data),
        ("val", val_data)
    ]:

        losses = torch.zeros(eval_iters)

        for k in range(eval_iters):

            x, y = get_batch(data)

            logits, loss = model(x, y)

            losses[k] = loss.item()

        results[split] = losses.mean().item()

    model.train()

    return results


# 8. Start training
print("\nStarting Transformer training...\n")

training_history = []

for step in range(max_iters):

    if step % eval_interval == 0:

        losses = estimate_loss()

        print(
            f"Step {step}: "
            f"Train Loss: {losses['train']:.4f}, "
            f"Validation Loss: {losses['val']:.4f}"
        )

        training_history.append({
            "step": step,
            "train_loss": losses["train"],
            "val_loss": losses["val"]
        })

    x, y = get_batch(train_data)

    logits, loss = model(x, y)

    optimizer.zero_grad(set_to_none=True)

    loss.backward()

    optimizer.step()


# 9. Final evaluation
final_losses = estimate_loss()

print("\nTraining completed!")

print("Final training loss:", final_losses["train"])
print("Final validation loss:", final_losses["val"])


# 10. Save training history
with open(
    "training_history.csv",
    "w",
    newline=""
) as file:

    writer = csv.DictWriter(
        file,
        fieldnames=[
            "step",
            "train_loss",
            "val_loss"
        ]
    )

    writer.writeheader()
    writer.writerows(training_history)


print("\nTraining history saved successfully!")

# Save trained Transformer model
torch.save(
    model.state_dict(),
    "trained_model.pth"
)

print("Trained model saved successfully!")