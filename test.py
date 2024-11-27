import torch

device = torch.device("cuda" if torch.cuda.is_available() else "CPU")

print(f"using device: {device}")

devNumber = torch.cuda.current_device()

print(f"Current device number is : {devNumber}")

devName = torch.cuda.get_device_name(devNumber)

print(f"GPU name is : {devName}")