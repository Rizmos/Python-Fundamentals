#Program that prompts
#user to enter  number chekcs
#whether a number is prime or not

def check_prime(num):
    if num <= 1:
        return False
    for i in range(2,int(num**0.5)+1):
        if num % i == 0:
             return False
    return True




num =int(input("Enter a number: "))
if check_prime(num):
    print( num ," is a prime number")

else :
    print( num ," is not a prime number")