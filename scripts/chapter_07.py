# Optimize J(w) = (w - 3)^2 with gradient 2(w-3).
w = -1.0
for _ in range(30):
    gradient = 2*(w-3)
    w -= 0.1*gradient
print('Final weight:', round(w, 5))
print('Final loss:', round((w-3)**2, 9))
