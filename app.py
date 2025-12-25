import torch

RANDOM_SEED = 42
torch.manual_seed(seed=RANDOM_SEED)
random_tensor_c = torch.rand(3, 4)
torch.manual_seed(seed=RANDOM_SEED)
random_tensor_d = torch.rand(3, 4)
print(random_tensor_c)
print(random_tensor_d)