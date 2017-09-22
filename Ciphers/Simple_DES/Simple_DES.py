import numpy as np
def permutation(P,K):
    n=list()
    for v in P:
        n.append(K[v-1])
    return n 

def sbox(v,s):
    res=s[int('0b'+str(v[0])+str(v[3]),base=2)][int('0b'+str(v[1])+str(v[2]),base=2)]
    return res

def keygen(inkey):
    inkey=permutation(p10, inkey) #P10 permutation
    left_inkey=list(inkey[0:5])   #Left
    right_inkey=list(inkey[5:11]) #Right
    left_inkey=np.roll(left_inkey,-1)   #Left shift
    right_inkey=np.roll(right_inkey,-1) #Left Shift
    inkey=list(list(left_inkey)+list(right_inkey)) #concat list
    #inkey=sum([left_inkey,right_inkey],[])
    key1=permutation(p8, inkey)     #Key1
    #Key2 Generation start
    left_inkey=np.roll(left_inkey,-2)   #Left shift by 2
    right_inkey=np.roll(right_inkey,-2) #left shift by 2
    inkey=list(list(left_inkey)+list(right_inkey))  #concat
    key2=permutation(p8, inkey) #P8 permutation
    keys=[key1,key2]    
    return keys

def encryption(pt,key1):  
    left_pt=list(pt[0:4])
    right_pt=list(pt[4:8])
    right_pt1=list(right_pt)
    right_pt=permutation(ep, right_pt)  #Extended permutation
    right_pt=np.bitwise_xor(key1,right_pt)  #key XOR Rightpart
    #s-box code
    left_sbox=list(right_pt[0:4])
    right_sbox=list(right_pt[4:8])
    left_sbox=list(bin(sbox(left_sbox,s0))) #Sbox
    right_sbox=list(bin(sbox(right_sbox,s1))) #Sbox
    left_sbox=left_sbox[2:]
    right_sbox=right_sbox[2:]
    if len(left_sbox)==1:
        #left_sbox=['0']+list(left_sbox)
        left_sbox.insert(0,'0')
    if len(right_sbox)==1:
        right_sbox.insert(0,'0')
        #right_sbox[0]=['0']+list(right_sbox)
    left1=list()
    right1=list()
    for e in left_sbox:
        left1.append(int(e))
    for e in right_sbox:
        right1.append(int(e))
    sbox1=list(list(left1)+list(right1))    
    sbox1=permutation(p4, sbox1)    #p4 permuatation to sbox output
    cip=np.bitwise_xor(sbox1,left_pt)   # Permutate output XOR Left part
    cip=list(list(right_pt1)+list(cip)) 
    return cip 

inkey=list(map(int,input('Enter Key:').split()))
pt=list(map(int,input('Enter Plain TEXT:').split()))
p10=[3,5,2,7,4,10,1,9,8,6]
p8=[6,3,7,4,8,5,10,9]
ip=[2,6,3,1,4,8,5,7]
ipinv=[4,1,3,5,7,2,8,6]
ep=[4,1,2,3,2,3,4,1]
p4=[2,4,3,1]
s0=np.array([[0b01,0b00,0b11,0b10],[0b11,0b10,0b01,0b00],[0b00,0b10,0b01,0b11],[0b11,0b01,0b11,0b10]])
s1=np.array([[0b00,0b01,0b10,0b11],[0b10,0b00,0b01,0b11],[0b11,0b00,0b01,0b00],[0b10,0b01,0b00,0b11]])
keys=keygen(inkey)
pt=permutation(ip, pt)  
cip=encryption(pt, keys[0])
cip=encryption(cip, keys[1])
cip=cip[4:8]+cip[0:4] 
cip=permutation(ipinv, cip)
print("Cipher Text:", end='')
for v in cip:
    print(v,end=' ')