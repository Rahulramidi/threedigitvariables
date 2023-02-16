def  isprime(n):
    if n<=1:
        return False
    for i in range (2,n/2):
        if n%i==0:
            return False
    return True

number=int(input("enter a number :"))
if isprime(number)==True: 
   print("prime number ")
print("not a prime number")
     
