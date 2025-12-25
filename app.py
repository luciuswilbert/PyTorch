import torch

tensors = torch.arange(0, 100, 10)
tensors = tensors.type(torch.float32)

print(tensors.min())
print(tensors.max())
print(tensors.mean())
print(tensors.sum())