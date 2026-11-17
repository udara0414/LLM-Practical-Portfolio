import torch
import gradio as gr

from model import TinyTransformer, vocab_size, block_size

# Load training data and vocabulary
checkpoint = torch.load(
    "training_data.pt",
    map_location="cpu",
    weights_only=False
)

stoi = checkpoint["stoi"]
itos = checkpoint["itos"]

# Load trained model
model = TinyTransformer()

model.load_state_dict(
    torch.load(
        "trained_model.pth",
        map_location="cpu",
        weights_only=True
    )
)

model.eval()

print("Trained Transformer model loaded successfully!")


# Generate text
def generate_text(prompt, max_tokens):

    if not prompt.strip():
        return "Please enter a prompt."

    try:
        # Convert prompt characters into token IDs
        context = torch.tensor(
            [[stoi[ch] for ch in prompt if ch in stoi]],
            dtype=torch.long
        )

        if context.size(1) == 0:
            return "No recognized characters in the prompt."

        # Generate new characters
        with torch.no_grad():
            generated = model.generate(
                context,
                max_new_tokens=int(max_tokens)
            )

        # Convert token IDs back into text
        result = "".join(
            [itos[i] for i in generated[0].tolist()]
        )

        return result

    except Exception as e:
        return f"Error: {str(e)}"


# Create Gradio interface
demo = gr.Interface(
    fn=generate_text,
    inputs=[
        gr.Textbox(
            label="Enter your prompt",
            placeholder="Once upon a time..."
        ),
        gr.Slider(
            minimum=50,
            maximum=300,
            value=150,
            step=50,
            label="Maximum characters to generate"
        )
    ],
    outputs=gr.Textbox(
        label="Generated Story",
        lines=10
    ),
    title="Tiny Transformer Language Model",
    description="Generate stories using a character-level Transformer model."
)


if __name__ == "__main__":
    demo.launch(
        server_name="127.0.0.1",
        server_port=7860,
        share=True
    )