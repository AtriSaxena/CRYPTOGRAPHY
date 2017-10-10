import numpy as np
from numpy.core.test_rational import gcd
import Extended_GCD
from Extended_GCD import Extended_euclid
def isprime(n):
    for i in range(2,n//2):
        if (n%i)==0:
            return False    
    return True

def encryption():
    msg=int(input("Enter Message:"))
    c=pow(msg,e)%n
    print("Cipher text:{}",format(c))
def decryption():
    c=int(input("Enter Encrypted message:"))
    m=pow(c,d)%n
    print("Decrypted message: {}".format(m))

f=0
while f==0:
    p=np.random.randint(3,40)
    if isprime(p):
        f=1
f=0
while f==0:
    q=np.random.randint(3,40)
    if isprime(q):
        f=1
n=p*q
toitent=(p-1)*(q-1)
for i in range(10,toitent):
    if gcd(i,toitent)==1:
        e=i
        break
d=Extended_euclid(toitent,e)%toitent
print("Public Key: {},{}".format(e,n))
print("Private Key: {}".format(d))
while(1):
    ch=int(input("1. Encrypt Message \n2. Decrypt Message \n3. Exit"))
    if ch==1:
        encryption()
    elif ch==2:
        decryption()
    elif ch==3:
        exit()
    else:
        print("Enter Choice Again")
        
