import flwr as fl
import torch
import torch.nn as nn
from model import get_model, get_optimizer

# Define the Flower server class
class FlowerServer(fl.server.Server):
    def __init__(self):
        super().__init__()
        self.model = get_model()  # Initialize the model
        self.optimizer = get_optimizer()  # Initialize the optimizer
    
    def fit(self, parameters: dict) -> dict:
        # Set model parameters received from the clients
        self.model.load_state_dict(parameters)
        
        # Dummy data
        data = torch.tensor([[1.0]])
        target = torch.tensor([[2.0]])

        # Training loop (one step for simplicity)
        self.model.train()
        criterion = nn.MSELoss()
        self.optimizer.zero_grad()
        output = self.model(data)
        loss = criterion(output, target)
        loss.backward()
        self.optimizer.step()

        # Return updated model parameters and loss
        return {"parameters": self.model.state_dict(), "loss": loss.item()}

    def evaluate(self, parameters: dict) -> dict:
        # Set model parameters received from the clients
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

def start_server():
    strategy = fl.server.strategy.FedAvg(
        min_fit_clients=1,
        min_evaluate_clients=1,
        min_available_clients=1,
    )
    fl.server.start_server(strategy=strategy, server_address="localhost:8080")

if __name__ == "__main__":
    start_server()
