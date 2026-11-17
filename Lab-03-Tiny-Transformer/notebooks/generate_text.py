import torch

from model import TinyTransformer, vocab_size, block_size


# 1. Select device
device = "cuda" if torch.cuda.is_available() else "cpu"


# 2. Load prepared data
checkpoint = torch.load(
    "training_data.pt",
    map_location="cpu",
    weights_only=False
)

stoi = checkpoint["stoi"]
itos = checkpoint["itos"]


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

print("Trained Transformer model loaded successfully!")


# 4. Define text generation function
@torch.no_grad()
def generate(idx, max_new_tokens=300):

    for _ in range(max_new_tokens):

        # Crop context to block size
        idx_cond = idx[:, -block_size:]

        # Get predictions
        logits, loss = model(idx_cond)

        # Select last character prediction
        logits = logits[:, -1, :]

        # Convert logits into probabilities
        probabilities = torch.softmax(logits, dim=-1)

        # Sample next character
        next_character = torch.multinomial(
            probabilities,
            num_samples=1
        )

        # Add generated character
        idx = torch.cat(
            (idx, next_character),
            dim=1
        )

    return idx


# 5. Generate text from a starting prompt
prompt = "Once upon a time"

# Encode prompt
context = torch.tensor(
    [[stoi[ch] for ch in prompt]],
    dtype=torch.long,
    device=device
)

# Generate new text
generated = generate(
    context,
    max_new_tokens=300
)

# Decode generated text
generated_text = "".join(
    [itos[i] for i in generated[0].tolist()]
)


# 6. Display generated story
print("\nGenerated Story:")
print("-" * 50)
print(generated_text)