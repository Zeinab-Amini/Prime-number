#Write your code below this line 👇
def prime_checker(number):
    prime = True
    for f in range(2, number):
        if number % f ==0:
            prime = False
    if prime:
            print("It is a prime number. ")
    else:
         print("It is not a prime number. ")

#Write your code above this line 👆
    
#Do NOT change any of the code below👇
n = int(input("Check this number: "))
prime_checker(number=n)