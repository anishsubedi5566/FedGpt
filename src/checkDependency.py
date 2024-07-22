try:
    import torch
    import torchvision
    import flwr
    print("All required packages are installed.")
except ImportError as e:
    print(f"Missing package: {e.name}")
