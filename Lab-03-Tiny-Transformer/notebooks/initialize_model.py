
import torch
import torch.nn as nn

from model import (
    TinyTransformer,
    vocab_size,
    block_size,
    n_embd,
    n_head,
    n_layer,
    dropout
)

# Load prepared training data
checkpoint = torch.load(
    "training_data.pt",
    map_location="cpu",
    weights_only=False
)

print("Training data loaded successfully!")


# Initialize Transformer model
model = TinyTransformer()

# Configure loss function
criterion = nn.CrossEntropyLoss()

# Configure optimizer
learning_rate = 0.001

optimizer = torch.optim.AdamW(
    model.parameters(),
    lr=learning_rate
)

# Count trainable parameters
total_params = sum(
    p.numel()
    for p in model.parameters()
    if p.requires_grad
)

# Save complete model configuration
model_config = {
    "vocab_size": vocab_size,
    "block_size": block_size,
    "n_embd": n_embd,
    "n_head": n_head,
    "n_layer": n_layer,
    "dropout": dropout,
    "learning_rate": learning_rate,
    "total_parameters": total_params
}

torch.save(
    model_config,
    "model_config.pt"
)

print("\nModel configuration saved successfully!")

print("\nSaved configuration:")
for key, value in model_config.items():
    print(f"{key}: {value}")
