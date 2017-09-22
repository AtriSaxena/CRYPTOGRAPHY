strg=str(input("Enter String"))
key=str(input("Enter Key"))
i=0
for c in strg:
    asci=ord(c)
    if asci>=97 & asci<=122:
        asci=asci+(ord(key[i])-97)
    if asci>122:
        asci=asci%122 +96
    print(chr(asci),end='')
    i=i+1
    if i>=len(key):
        i=0