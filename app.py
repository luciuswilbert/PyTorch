import torch

data_a = torch.randn(2, 3, 5)
print(data_a.view(2, 15))