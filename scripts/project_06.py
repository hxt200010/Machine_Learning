# Image classification in PyTorch
# Public scikit-learn digits images processed by a small PyTorch MLP (fully connected image classifier for fast reproducibility).
import numpy as np
import torch
from sklearn.datasets import load_digits
from sklearn.model_selection import train_test_split
torch.manual_seed(7)
X,y=load_digits(return_X_y=True)
a,b,c,d=train_test_split(X/16.,y,test_size=.2,stratify=y,random_state=42)
a=torch.tensor(a,dtype=torch.float32);b=torch.tensor(b,dtype=torch.float32)
c=torch.tensor(c,dtype=torch.long);d=torch.tensor(d,dtype=torch.long)
net=torch.nn.Sequential(torch.nn.Linear(64,64),torch.nn.ReLU(),torch.nn.Linear(64,10))
opt=torch.optim.Adam(net.parameters(),lr=.01)
for _ in range(18):
    opt.zero_grad();loss=torch.nn.functional.cross_entropy(net(a),c)
    loss.backward();opt.step()
with torch.no_grad():
    acc=float((net(b).argmax(1)==d).float().mean())
print('Holdout image accuracy:',round(acc,3))
print('Input features:',a.shape[1])
