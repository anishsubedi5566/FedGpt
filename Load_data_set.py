import torchvision.datasets as datasets
import torchvision.transforms as transforms

# Define the transformation (convert to tensor and normalize)
transform = transforms.Compose([transforms.ToTensor()])

# Download the training and test datasets
train_dataset = datasets.MNIST(root='data', train=True, download=True, transform=transform)
test_dataset = datasets.MNIST(root='data', train=False, download=True, transform=transform)
