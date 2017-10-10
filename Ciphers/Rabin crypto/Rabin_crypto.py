import numpy as np
import Extended_GCD
from Extended_GCD import Extended_euclid

def encryption(p):
    c=p*p%public_k
    return c

def decryption(c):
    a1=int(pow(c,(p+1)/4)%p)
    a2=int((-pow(c,(p+1)/4))%p)
    b1=int(pow(c,(q+1)/4)%q) 
    b2=int(-pow(c,(q+1)/4)%q)
    X=list()
    X.append(Chinese_Remainder(a1, b1, p, q))
    X.append(Chinese_Remainder(a1, b2, p, q))
    X.append(Chinese_Remainder(a2, b1, p, q))
    X.append(Chinese_Remainder(a2, b2, p, q))
    return X
def Chinese_Remainder(a,b,p,q):
    M=p*q 
    M1=M/p 
    M2=M/q 
    M1_inv=Extended_euclid(p,M1)

    M2_inv=Extended_euclid(q,M2)
    X=int(((a*M1*M1_inv)+(b*M2*M2_inv))%M)
    if X<0:
        q=-X//M
        X=X+(M*(q+1))
    X=X%M
    return X 
#key generation
p=np.random.randint(0,50)
q=np.random.randint(0,50)
print("P={},Q={}".format(p,q))
n=p*q
public_k=n
private_k=[q,n]
p=int(input("Enter plain text"))        
c=encryption(p)
print(c)
X=decryption(c)
print("Possible Decrypted Text: {}".format(X))