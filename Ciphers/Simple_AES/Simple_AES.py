import numpy as np
def adj(mrow):
    if len(mrow)==3:
        mrow.insert(0, 0)
    elif len(mrow)==2:
        mrow.insert(0,0)
        mrow.insert(0,0)
    elif len(mrow)==1:
        mrow.insert(0,0)
        mrow.insert(0,0)
        mrow.insert(0,0)
    return mrow
    
def subnib(k):
    lt=int("0b"+str(k[0])+str(k[1])+str(k[2])+str(k[3]),base=2)
    res=list(sbox[lt])
    if len(k)>4:
        lt=int("0b"+str(k[4])+str(k[5])+str(k[6])+str(k[7]),base=2)
        res1=list(sbox[lt])
        r=list(list(res)+list(res1))
        r=list(map(int,r))
        return r 
    else:
        return res
    
def key_generation(key):
    w0=list(key[0:8])
    w1=list(key[8:16])
    keys=list()
    keys.append(key)#key0
    w2=list(np.bitwise_xor(w0,np.bitwise_xor([1,0,0,0,0,0,0,0],subnib(np.roll(w1,-4)))))
    w3=list(np.bitwise_xor(w2,w1))
    #print(w3)
    w4=list(np.bitwise_xor(w2,np.bitwise_xor([0,0,1,1,0,0,0,0],subnib(np.roll(w3,-4)))))
    #print(w4)
    w5=list(np.bitwise_xor(w4,w3))
    keys.append(list(w2)+list(w3))
    keys.append(list(w4)+list(w5))
    return keys

def encryption(ip,f):
    op=list(subnib(ip[0:4])+subnib(ip[4:8])+subnib(ip[8:12])+subnib(ip[12:16])) #SBOX
    op=list(op[0:4]+op[12:16]+op[8:12]+op[4:8])
    if f==1:    #Final Round not require mix column
        op=list(map(int,op))
        return op
    vw=str('0b'+str(op[8])+str(op[9])+str(op[10])+str(op[11]))
    mrow=list(bin(Ltable[3][int(vw,base=2)-1]))
    mrow=list(map(int,mrow[2:]))
    if len(mrow)<4:
        mrow=adj(mrow)
    s00=np.bitwise_xor(list(map(int,op[0:4])),mrow)
    vw=str('0b'+str(op[0])+str(op[1])+str(op[2])+str(op[3]))
    mrow=list(bin(Ltable[3][int(vw,base=2)-1]))
    mrow=list(map(int,mrow[2:]))
    if len(mrow)<4:
        mrow=adj(mrow)
    s10=np.bitwise_xor(mrow,list(map(int,op[8:12])))
    vw=str('0b'+str(op[12])+str(op[13])+str(op[14])+str(op[15]))    
    mrow=list(bin(Ltable[3][int(vw,base=2)-1]))
    mrow=list(map(int,mrow[2:]))
    if len(mrow)<4:
        mrow=adj(mrow)
    s01=np.bitwise_xor(list(map(int,op[4:8])),mrow)
    vw=str('0b'+str(op[4])+str(op[5])+str(op[6])+str(op[7]))
    mrow=list(bin(Ltable[3][int(vw,base=2)-1]))
    mrow=list(map(int,mrow[2:]))
    if len(mrow)<4:
        mrow=adj(mrow)
    s11=np.bitwise_xor(mrow,list(map(int,op[12:16])))
    op=list(list(s00)+list(s10)+list(s01)+list(s11))
    return op
    
key=list(map(int,input("Enter Key:").split()))
pt=list(map(int,input("Enter Plain Text:").split()))
sbox=['1001','0100','1010','1011','1101','0001','1000','0101','0110','0010','0000','0011','1100','1110','1111','0111']
Ltable=[[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15],
        [2,4,6,8,10,12,14,3,1,5,7,5,11,9,15,13],
        [3,6,5,12,15,10,9,11,8,13,14,7,4,1,2],
        [4,8,12,3,7,11,15,6,2,14,10,5,1,13,9],
        [5,10,15,7,2,13,8,14,11,4,1,9,12,3,6],
        [6,12,10,11,13,7,1,5,3,9,15,14,8,2,4],
        [7,14,9,15,8,1,6,13,10,3,4,2,5,12,11],
        [8,3,11,6,14,5,13,12,4,15,7,10,2,9,1],
        [9,1,8,2,11,3,10,4,13,5,12,6,15,7,4],
        [10,7,13,14,4,9,3,15,5,8,2,1,11,6,12],
        [11,5,14,10,1,15,4,7,12,2,9,13,6,8,3],
        [12,11,7,5,9,14,2,10,6,1,13,15,3,4,8],
        [13,9,4,1,12,8,5,2,15,11,6,3,14,10,7],
        [14,15,1,13,3,2,12,9,7,6,8,4,10,11,5],
        [15,13,2,9,6,4,11,1,14,12,3,8,7,5,10]]

keys=key_generation(key)
ip=np.bitwise_xor(pt,keys[0])
op=encryption(ip,0)
ip=np.bitwise_xor(op,keys[1])
op=encryption(ip,1)
op=list(np.bitwise_xor(op,keys[2]))
print("Cipher Text: ",end='')
i=0
while i<=12:
    print(op[i],end='')
    print(op[i+1],end='')
    print(op[i+2],end='')
    print(op[i+3],end=' ')
    i=i+4