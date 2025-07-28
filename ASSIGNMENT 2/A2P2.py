import math
num=int(input("Enter the number:"))
sqrt=math.sqrt(num)
if not sqrt.is_integer():
    print(f"The square root {sqrt} is not a prime number.")
else:
    if sqrt<2:
        print(f"The square root {sqrt} is not a prime number.")
    else:
        for i in range (2,int(sqrt)//2):
            if(sqrt%i==0):
                print(f"The square root {sqrt} is not a prime number.")
                break
            
        else:
            print(f"The square root {sqrt} is a prime number")
                
                
                

    
