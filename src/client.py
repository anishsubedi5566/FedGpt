import flwr as fl
import torch
import torch.nn as nn
from model import get_model, get_optimizer

# Define the Flower client class
class FlowerClient(fl.client.Client):
    def __init__(self):
        self.model = get_model()  # Initialize the model
    
    def fit(self, fit_ins: fl.common.FitIns) -> dict:
        # Extract model parameters from fit_ins
        parameters = fit_ins.parameters
        
        # Set model parameters received from the server
        self.model.load_state_dict(parameters)
        
        # Dummy data
        data = torch.tensor([[1.0]])
        target = torch.tensor([[2.0]])

        # Training loop (one step for simplicity)
        criterion = nn.MSELoss()
        output = self.model(data)
        loss = criterion(output, target)
        self.model.train()  # Ensure the model is in training mode
        self.optimizer = get_optimizer()  # Initialize the optimizer
        self.optimizer.zero_grad()
        loss.backward()
        self.optimizer.step()

        # Return updated model parameters and loss
        return {"parameters": self.model.state_dict(), "loss": loss.item()}

    def evaluate(self, parameters: dict) -> dict:
        # Set model parameters received from the server
        self.model.load_state_dict(parameters)
        
        # Dummy data
        data = torch.tensor([[1.0]])
        target = torch.tensor([[2.0]])

        # Evaluation
        self.model.eval()
        criterion = nn.MSELoss()
        output = self.model(data)
        loss = criterion(output, target)

        # Return evaluation results
        return {"loss": loss.item()}

# def start_client():
#     fl.client.start_numpy_client(server_address="localhost:8080", client=FlowerClient())
    
def start_client():
    # Create a FlowerClient instance
    client = FlowerClient().to_client()
    
    # Start the Flower client
    fl.client.start_client(
        server_address="localhost:8080",
        client=client
    )

if __name__ == "__main__":
    start_client()
