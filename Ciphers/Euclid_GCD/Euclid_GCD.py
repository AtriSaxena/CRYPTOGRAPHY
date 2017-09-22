def euclid_gcd(num1,num2):
    if int(num2)==0:
        return num1
    else:
        return (euclid_gcd(num2,num1 % num2)) 
    

def main():
    num1 = input("Enter number to find GCD")
    num2 = input("Enter number to find GCD")
    ans=euclid_gcd(num1,num2)
    print("GCD is {}".format(int(ans))
          
        

if __name__=='__main__':main()