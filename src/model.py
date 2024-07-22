import torch
import torch.nn as nn
import torch.optim as optim

# Define a simple neural network model
class SimpleModel(nn.Module):
    def __init__(self):
        super(SimpleModel, self).__init__()
        self.fc = nn.Linear(1, 1)
    
    def forward(self, x):
        return self.fc(x)

# Function to get a new instance of the model
def get_model():
    return SimpleModel()

# Function to get an optimizer for the model
def get_optimizer(model):
    return optim.SGD(model.parameters(), lr=0.01)  # Stochastic Gradient Descent optimizer

# Example usage
if __name__ == "__main__":
    model = get_model()  # Create model instance
    optimizer = get_optimizer(model)  # Create optimizer for the model

    # Print model parameters and optimizer to verify
    print("Model parameters:", list(model.parameters()))
    print("Optimizer:", optimizer)
