import numpy as np

from Extended_GCD import Extended_euclid
def Signing(d):
    print("Signing Stage:")
    M=int(input("\tEnter message: "))
    r=np.random.randint(10,100)
    print("\tAlice selects secret number:{} ".format(r))
    #r=307
    S1=pow(e1,r)%p
    S2=((M-d*S1)*Extended_euclid(p-1,r))%(p-1)
    print("\tS1= {} , S2= {}".format(S1,S2))
    print("\tAlice send S1, S2 & M value to Bob.")
    
def Verifying(public_k):
    print("Verifying Stage:")
    S1=int(input("\tenter S1 :"))
    S2=int(input("\tEnter S2: "))
    M=int(input("\tEnter message:"))
    if S1<0 and S1>public_k[2]:
        print("\tS1 is not Correct")
    elif S2<0 and S2>public_k[2]-1:
        print("\tS2 is not correct")
    else:
        V1=pow(public_k[0],M)%p 
        V2=pow(public_k[1],S1)*pow(S1,S2)%p
        if V1==V2:
            print("\tMessage is Accepted.")
        else:
            print("\tMessage is Rejected.")
def isprime(num):
    for i in range(2,num//2):
        if num%i==0:
            return 0
    return 1
def primitive_root(num):
    for i in range(3,num):
        flag=0
        root=list()
        for j in range(0,num-2):
            res=pow(i,j)%num
            if res in root:
                flag=1
                break
            else:
                root.append(res)
        if flag==0:
            return i
#key generation     
while(1):
    p=np.random.randint(10,100)
    if isprime(p):
        e1=primitive_root(p)
        if e1!=None:
            break
d=np.random.randint(2,p-2)
#p=3119
#e1=2
#d=127
e2=pow(e1,d)%p
public_key =[e1,e2,p]
private_key=d


Signing(d)
Verifying(public_key)