import torch

data = torch.randn(3, 3)
print(data, torch.argmax(data), torch.argmin(data))