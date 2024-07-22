import flwr as fl
import torch
import torch.nn as nn
from model import get_model, get_optimizer

#Define the Flower server class

class FlowerServer(fl.server.Server):
    def __init__(self):
        super().__init__()
        self.model = get_model() #Initialize the model
        self.optimizer = get_optimizer() #Initalize the optimizer
    
    def fit(self, parameters):
        #set model parameters received from the clients
        self.model.load_state_dict(parameters)

        #Dumy data
        data = torch.tensor([[1.0]])
        target = torch.tensor([[2.0]])

        #Training loop (one step for simplicity)
        self.model.train()
        criterion = nn.MSELoss()
        self.optimizer.zero_grad()
        output = self.model(data)
        loss = criterion(output, target)
        loss.backward()
        self.optimizer.step()


        #return updated model parameters
        return self.model.state_dict()

def start_server():
    strategy = fl.server.strategy.FedAvg(
        min_fit_clients=1,
        min_evaluate_clients=1,
        min_available_clients=1,
    )
    fl.server.start_server(strategy=strategy)

if __name__ == "__main__":
    start_server()