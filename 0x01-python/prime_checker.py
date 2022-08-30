import numbers
def prime_checker(number):
    flag = False
    
    for i in range(2,number):
        if number % i == 0:
            flag = True
            break
    if flag == True:
        print("This is not a prime number")
    else:
        print("This is a prime number")
        

n = int(input("Enter a number: "))
prime_checker(number=n)