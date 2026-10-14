# Minimal Transformer model
# Synthetic token sequences with class equal to whether token 1 appears; a small Transformer encoder is trained and evaluated.
import numpy as np
import torch
torch.manual_seed(7)
rng=np.random.default_rng(7)
X=rng.integers(1,20,size=(250,6));y=(X==1).any(axis=1).astype(int)
train=200
xtr=torch.tensor(X[:train],dtype=torch.long);xte=torch.tensor(X[train:],dtype=torch.long)
ytr=torch.tensor(y[:train],dtype=torch.long);yte=torch.tensor(y[train:],dtype=torch.long)
class TinyTransformer(torch.nn.Module):
    def __init__(self):
        super().__init__()
        self.emb=torch.nn.Embedding(20,16)
        self.pos=torch.nn.Embedding(6,16)
        self.enc=torch.nn.TransformerEncoderLayer(d_model=16,nhead=2,dim_feedforward=32,batch_first=True,dropout=0)
        self.out=torch.nn.Linear(16,2)
    def forward(self,x):
        h=self.emb(x)+self.pos(torch.arange(x.shape[1]))
        return self.out(self.enc(h).mean(1))
net=TinyTransformer();opt=torch.optim.Adam(net.parameters(),lr=.01)
for _ in range(18):
    opt.zero_grad();loss=torch.nn.functional.cross_entropy(net(xtr),ytr)
    loss.backward();opt.step()
with torch.no_grad():acc=float((net(xte).argmax(1)==yte).float().mean())
print('Holdout accuracy:',round(acc,3))
print('Baseline negative class accuracy:',round(float((yte==0).float().mean()),3))
print('Token sequence length:',xtr.shape[1])
