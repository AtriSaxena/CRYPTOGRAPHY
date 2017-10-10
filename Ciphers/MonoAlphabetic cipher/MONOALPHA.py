cipAlp=list(map(str,input("Enter CipherText Alphabet").split()))
plainText=str(input("Enter Plain Text:"))
plainText=str.upper(plainText)
print("Cipher Text:",end='')
for v in plainText:
    ind=ord(v)-ord('A')
    print(cipAlp[ind],end='')