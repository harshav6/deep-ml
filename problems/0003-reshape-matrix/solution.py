import torch

def reshape_matrix(a, new_shape) -> torch.Tensor:
    # Dimension check
    if len(a) * len(a[0]) != new_shape[0] * new_shape[1]:
        return torch.tensor([])
    # Convert to tensor and reshape
    a_t = torch.as_tensor(a, dtype=torch.float)
    
    return a_t.reshape(new_shape)
    
    pass
