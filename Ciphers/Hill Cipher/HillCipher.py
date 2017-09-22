import numpy
import Extended_GCD
M,N=map(int,input().split())
def matrix(x,y,initial):
    return [[initial for i in range(x)] for j in range(y)]

my_matrix=matrix(N,M,0)
print("Enter key:")
for i in range(0,M):
    for j in range(0,N):
        my_matrix[j][i]=int(input())
def Encryption():
    st=input("Enter message:")
    st=st.upper()
    st=st.replace(" ", "")
    l=len(st)//N
    msg_matrix=matrix(N,l,0)
    k=0
    for i in range(0,l):
        for j in range(0,N):
            msg_matrix[i][j]=(ord(st[k]))%65
            k+=1
    prod=[[0 for x in range(N)]for y in range(M)]
    #print(msg_matrix)
    sum=0
    prod=numpy.dot(msg_matrix,my_matrix)
    #print(prod)
    print("Cipher text:")
    for j in range(0,l):
            for k in range(0,M):
                print(chr(prod[j][k]%26+65),end="")
def decryption():
    ct=input("Enter Cipher text:")
    ct=ct.upper()
    ct=ct.replace(" ", "")
    l=len(ct)//N
    cipher_matrix=matrix(N,l,0)
    k=0
    for i in range(0,l):
        for j in range(0,N):
            cipher_matrix[i][j]=(ord(ct[k]))%65
            k+=1
    det=(numpy.linalg.det(my_matrix))%26
    det=Extended_GCD.Extended_euclid(26, det)
    trs=my_matrix
    minr=matrix(3,3,0)
    minr[0][0]=(trs[1][1]*trs[2][2]-trs[2][1]*trs[1][2])
    minr[0][1]=-(trs[1][0]*trs[2][2]-trs[2][0]*trs[1][2])
    minr[0][2]=trs[1][0]*trs[2][1]-trs[2][0]*trs[1][1]
    minr[1][0]=-(trs[0][1]*trs[2][2]-trs[2][1]*trs[0][2])
    minr[1][1]=trs[0][0]*trs[2][2]-trs[2][0]*trs[0][2]
    minr[1][2]=-(trs[0][0]*trs[2][1]-trs[2][0]*trs[0][1])
    minr[2][0]=(trs[0][1]*trs[1][2]-trs[1][1]*trs[1][2])
    minr[2][1]=-(trs[0][0]*trs[1][2]-trs[1][0]*trs[1][2])
    minr[2][2]=(trs[0][0]*trs[1][1]-trs[1][0]*trs[0][1])
    minr=numpy.array(minr)
    minr=(minr*det)%26
    print("TEXT:")
    minr=numpy.transpose(minr)
    minr=numpy.dot(cipher_matrix,minr)
    for j in range(0,l):
            for k in range(0,M):
                print(chr(minr[j][k]%26+65),end="")

while (1):
    choice=int(input("\n 1.Encryption \n 2.Decryption: \n 3.EXIT"))
    if choice==1:
        Encryption()
    elif choice==2:
        decryption()
    elif choice==3:
        exit()
    else:
        print("Choose correct choice")