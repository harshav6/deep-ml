import torch
import torch.nn.functional as F
import math

def softmax(scores: list[float]) -> list[float]:

  result = [math.exp(z) for z in scores]
  total = sum(result)
  softmax_scores = [round(x / total, 4) for x in result]

  return softmax_scores
  pass
