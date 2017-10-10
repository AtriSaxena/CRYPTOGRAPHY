def rc(key):
    keylen=len(key)
    for i in range(0,256):
        s.append(i)
        K.append(ord(key[i%keylen]))
    j=0
    for i in range(0,256):
        j=(j+s[i]+K[i])%256
        s[i],s[j]=s[j],s[i]
    msg=list(input("Enter msg:"))
    i=0
    j=0
    print("Cipher Text:")
    for v in msg:
        i=(i+1)%256
        j=(j+s[i])%256
        s[i],s[j]=s[j],s[i]
        k=s[(s[i] + s[j]) % 256]
        C=ord(v)^k
        print("%02X" %C,end='')
    return 0

key=list(input("Enter key"))
s=list()
K=list()
rc(key)
