import torch

tensors = torch.arange(1., 8.)
reshaped_tensors = tensors.reshape(1, 7)
print(reshaped_tensors)