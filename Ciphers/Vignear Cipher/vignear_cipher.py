strg=str(input("Enter String"))
strg=str.lower(strg)
strg=strg.replace(" ","")
key=str(input("Enter Key"))
key=str.lower(key)
i=0
key_len=len(key)
for c in strg:
    asci=ord(c)
    if asci>=97 and asci<=122:
        asci=asci+(ord(key[i])-97)
    if asci>122:
        asci=asci%122 +96
    #asci=asci+32
    print(chr(asci-32),end='')
    i=(i+1)%key_len
    if i>=len(key):
        i=0
