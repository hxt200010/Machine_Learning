import numpy as np
# Deterministic tabular Q-learning in a 5-state corridor.
q=np.zeros((5,2))  # 0=left, 1=right
rng=np.random.default_rng(7)
for episode in range(500):
    state=0
    for _ in range(20):
        action=int(rng.integers(2)) if rng.random()<0.1 else int(np.argmax(q[state]))
        nxt=max(0,state-1) if action==0 else min(4,state+1)
        reward=1.0 if nxt==4 else -0.01
        q[state,action]+=0.2*(reward+0.9*np.max(q[nxt])-q[state,action])
        state=nxt
        if state==4: break
print('Action values in starting state:',q[0].round(3).tolist())
print('Greedy action at start (1=right):',int(np.argmax(q[0])))
