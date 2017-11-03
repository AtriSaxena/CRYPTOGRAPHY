import numpy as np
g=7
p=23
x=np.random.randint(2,100)
print("Alice select random number x:{}".format(x))
y=np.random.randint(2,100)
print("Bob select random number x:{}".format(y))
R1=pow(g,x)%p
R2=pow(g,y)%p
print("Alice sends R1:{} to Bob".format(R1))
print("Bob sends R1:{} to Alice".format(R2))
K=pow(R2,x)%p
print("Alice Calculates K:{}".format(K))
K=pow(R1,y)%p
print("Bob Calculates K:{}".format(K))