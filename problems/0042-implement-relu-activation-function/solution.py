import torch

def relu(z: float) -> torch.Tensor:
    return torch.tensor(round(z,1) if z>0 else 0.0)
    pass
