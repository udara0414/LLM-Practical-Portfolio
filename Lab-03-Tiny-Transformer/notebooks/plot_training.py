import pandas as pd
import matplotlib.pyplot as plt

# Load training history
data = pd.read_csv("training_history.csv")

# Display training history
print("Training history loaded successfully!")
print(data)

# Plot training and validation loss
plt.figure(figsize=(10, 6))

plt.plot(
    data["step"],
    data["train_loss"],
    label="Training Loss"
)

plt.plot(
    data["step"],
    data["val_loss"],
    label="Validation Loss"
)

# Add chart details
plt.title("Transformer Training and Validation Loss")
plt.xlabel("Training Steps")
plt.ylabel("Loss")

plt.legend()
plt.grid(True)

# Save graph
plt.savefig("loss_curve.png")

# Display graph
plt.show()

print("\nLoss curve saved successfully!")