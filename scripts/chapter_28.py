import torch
torch.manual_seed(7)
cnn=torch.nn.Sequential(torch.nn.Conv2d(1,4,kernel_size=3,padding=1),
  torch.nn.ReLU(),torch.nn.MaxPool2d(2))
x=torch.randn(2,1,8,8)
y=cnn(x)
print('Input tensor shape:',tuple(x.shape))
print('CNN feature map shape:',tuple(y.shape))
print('Trainable parameters:',sum(p.numel() for p in cnn.parameters()))
