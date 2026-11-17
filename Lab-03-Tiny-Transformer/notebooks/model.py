
import torch
import torch.nn as nn
import torch.nn.functional as F

# Model configuration
vocab_size = 75
block_size = 64
n_embd = 128
n_head = 8
n_layer = 3
dropout = 0.1


class Head(nn.Module):

    def __init__(self, head_size):
        super().__init__()

        self.key = nn.Linear(n_embd, head_size, bias=False)
        self.query = nn.Linear(n_embd, head_size, bias=False)
        self.value = nn.Linear(n_embd, head_size, bias=False)

        self.register_buffer(
            "tril",
            torch.tril(torch.ones(block_size, block_size))
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        B, T, C = x.shape

        k = self.key(x)
        q = self.query(x)

        weights = q @ k.transpose(-2, -1)
        weights = weights * (k.shape[-1] ** -0.5)

        weights = weights.masked_fill(
            self.tril[:T, :T] == 0,
            float("-inf")
        )

        weights = F.softmax(weights, dim=-1)
        weights = self.dropout(weights)

        v = self.value(x)
        output = weights @ v

        return output


class MultiHeadAttention(nn.Module):

    def __init__(self, num_heads, head_size):
        super().__init__()

        self.heads = nn.ModuleList([
            Head(head_size) for _ in range(num_heads)
        ])

        self.projection = nn.Linear(
            num_heads * head_size,
            n_embd
        )

        self.dropout = nn.Dropout(dropout)

    def forward(self, x):

        output = torch.cat(
            [head(x) for head in self.heads],
            dim=-1
        )

        output = self.projection(output)
        output = self.dropout(output)

        return output


class FeedForward(nn.Module):

    def __init__(self):
        super().__init__()

        self.network = nn.Sequential(
            nn.Linear(n_embd, 4 * n_embd),
            nn.ReLU(),
            nn.Linear(4 * n_embd, n_embd),
            nn.Dropout(dropout)
        )

    def forward(self, x):
        return self.network(x)


class TransformerBlock(nn.Module):

    def __init__(self):
        super().__init__()

        head_size = n_embd // n_head

        self.attention = MultiHeadAttention(
            n_head,
            head_size
        )

        self.feed_forward = FeedForward()

        self.layer_norm1 = nn.LayerNorm(n_embd)
        self.layer_norm2 = nn.LayerNorm(n_embd)

    def forward(self, x):

        x = x + self.attention(self.layer_norm1(x))
        x = x + self.feed_forward(self.layer_norm2(x))

        return x


class TinyTransformer(nn.Module):

    def __init__(self):
        super().__init__()

        self.token_embedding = nn.Embedding(
            vocab_size,
            n_embd
        )

        self.position_embedding = nn.Embedding(
            block_size,
            n_embd
        )

        self.blocks = nn.Sequential(
            *[TransformerBlock() for _ in range(n_layer)]
        )

        self.final_norm = nn.LayerNorm(n_embd)

        self.output_layer = nn.Linear(
            n_embd,
            vocab_size
        )

    def forward(self, idx, targets=None):

        B, T = idx.shape

        token_emb = self.token_embedding(idx)

        positions = torch.arange(T, device=idx.device)
        position_emb = self.position_embedding(positions)

        x = token_emb + position_emb
        x = self.blocks(x)
        x = self.final_norm(x)

        logits = self.output_layer(x)

        loss = None

        if targets is not None:

            B, T, C = logits.shape

            loss = F.cross_entropy(
                logits.reshape(B * T, C),
                targets.reshape(B * T)
            )

        return logits, loss

    # Generate new text
    @torch.no_grad()
    def generate(self, idx, max_new_tokens):

        for _ in range(max_new_tokens):

            idx_cond = idx[:, -block_size:]

            logits, loss = self(idx_cond)

            logits = logits[:, -1, :]

            probabilities = F.softmax(logits, dim=-1)

            next_idx = torch.multinomial(
                probabilities,
                num_samples=1
            )

            idx = torch.cat(
                (idx, next_idx),
                dim=1
            )

        return idx


if __name__ == "__main__":

    model = TinyTransformer()

    sample_input = torch.randint(
        0,
        vocab_size,
        (4, block_size)
    )

    sample_target = torch.randint(
        0,
        vocab_size,
        (4, block_size)
    )

    logits, loss = model(sample_input, sample_target)

    print("Transformer model created successfully!")
    print("Input shape:", sample_input.shape)
    print("Output shape:", logits.shape)
    print("Initial loss:", loss.item())

    total_params = sum(
        p.numel() for p in model.parameters()
    )

    print("Total parameters:", total_params)

