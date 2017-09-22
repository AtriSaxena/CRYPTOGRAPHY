string=str(input("input a String:"))
N=int(input("Enter length:"))
string=string.lower()
print("Encrypted String:",end='')
for c in string:
    asci=ord(c)
    if (asci>=97) & (asci <=122):
        asci+=N
    if asci>122:
        asci=asci%122 +96
    print(chr(asci),end='')    