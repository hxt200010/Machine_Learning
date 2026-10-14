import torch
torch.manual_seed(7)
net=torch.nn.Sequential(torch.nn.Linear(2,4),torch.nn.ReLU(),torch.nn.Linear(4,1))
x=torch.tensor([[1.,2.],[2.,1.]])
y=torch.tensor([[3.],[3.]])
optimizer=torch.optim.SGD(net.parameters(),lr=0.01)
for _ in range(30):
    optimizer.zero_grad()
    loss=((net(x)-y)**2).mean()
    loss.backward()
    optimizer.step()
print('Final MSE:',round(float(((net(x)-y)**2).mean().detach()),4))
print('Number of trainable parameters:',sum(p.numel() for p in net.parameters()))
