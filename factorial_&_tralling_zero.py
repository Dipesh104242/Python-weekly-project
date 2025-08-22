def find_factorial(n):
    
    if n == 0:
        return 1
    elif n == 1:
        return 1
        
    else:
        Total = 1
        for i in range(1,n+1):
            Total*=i
        return Total
def factorialTrailingZeros(number):
    fac = find_factorial(number)
    print(fac)
    count = 0
    while (fac%10 ==0):
        count = count + 1
        fac = fac/10
    return count

        
    
    
number = int(input("Enter here your integer number:\n"))

# print("Your factorial number is:\t",find_factorial(int(number)))
print(factorialTrailingZeros(number))