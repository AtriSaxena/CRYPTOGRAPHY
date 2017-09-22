import math
def Extended_euclid(m,b):
    A1,A2,A3=1,0,m
    B1,B2,B3=0,1,b 
    while(1):
        if B3==0:
            return B3
        elif B3==1:
            return B2
        Q=math.floor(A3/B3)
        T1=A1-Q*B1
        T2=A2-Q*B2
        T3=A3-Q*B3
        A1,A2,A3=B1,B2,B3
        B1,B2,B3=T1,T2,T3

#b,m=map(int,input("Enter 'B' & 'M' ").split())
#res=Extended_euclid(m, b)
#if res==0:
#    print("NO INVERSE")
#else:
#    print("Inverse: {}".format(res)) 