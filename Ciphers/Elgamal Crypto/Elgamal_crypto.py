import numpy as np
from Extended_GCD import Extended_euclid
def encryption(public_k):
    P=int(input("Enter Plain text"))
    r=4
    C1=pow(public_k[0],r)%public_k[2]
    C2=(P*pow(public_k[1],r))%public_k[2]
    print("Cipher Text:",end='')
    print("{} , {} ".format(C1,C2))
def decryption(private_k,p):
    C=list(map(int,input("Enter Cipher").split()))
    P=C[1]*Extended_euclid(p,pow(C[0],private_k))%p
    print("Decrypted text: {} ".format(P))

#key generation     
p=np.random.randint(10,100)
d=np.random.randint(1,p-2)
e1=2
e2=pow(e1,d)%p 
public_k =[e1,e2,p]
private_k=d
encryption(public_k)
decryption(private_k,p)