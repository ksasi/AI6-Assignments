```
This python file is a goood starting pouint.
Activation Functions
```

#libraries
import numpy as np

def sigmoid(x):
  # enter code below
  return (1 / (1 + numpy.exp(-x)))

def tanh(x):
  # enter code below
  return ((np.exp(x) - np.exp(-x))/(np.exp(x) + np.exp(-x)))
  
def relu(x):
  # entr code below
  if x > 0:
    return x
   else:
    return 0
    
  
