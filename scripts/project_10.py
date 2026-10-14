# Predictive maintenance
# Synthetic motor signals transformed to RMS and spectral features; pipeline fits equipment-state labels.
import numpy as np
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
from sklearn.dummy import DummyClassifier
rng=np.random.default_rng(8);n=240;N=128;fs=512
labels=np.r_[np.zeros(n//2,dtype=int),np.ones(n//2,dtype=int)]
features=[]
for y in labels:
    t=np.arange(N)/fs
    wave=np.sin(2*np.pi*40*t)+y*.7*np.sin(2*np.pi*90*t)+rng.normal(0,.15,N)
    mag=np.abs(np.fft.rfft(wave))
    features.append([np.sqrt(np.mean(wave**2)),mag[np.argmin(abs(np.fft.rfftfreq(N,1/fs)-90))]])
X=np.asarray(features)
a,b,c,d=train_test_split(X,labels,test_size=.25,stratify=labels,random_state=7)
for name,model in [('majority',DummyClassifier(strategy='most_frequent')),('forest',RandomForestClassifier(n_estimators=30,random_state=7))]:
    model.fit(a,c)
    print(name,'test accuracy:',round(model.score(b,d),3))
print('Important: all data are synthetic.')
