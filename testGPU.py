import torch

device = torch.device("cuda" if torch.cuda.is_available() else "cpu")
print("Using:", device)

x = torch.randn(1000, 1000).to(device)
y = torch.matmul(x, x)
print(y.device)
print("hello world")