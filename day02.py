#for dan in range (2, 10, 1):
#    for i in range(1, 10, 1):
#        print(f"{dan} * {i} = {dan*i}")

#dan = input("Input dan : ")
#for i in range(1, 10, 10):
#    print(f"{dan}")

n = int(input("Input number :"))

is_prime = True

if n>=2:
    for i in range(2, int(n**0.5) +1):
        if n %i == 0:
            # count = count +1
        is_prime = False
        break
        print(i, end=' ')
else:
    is_prime = False

if is_prime == True:
    print(f"{n} is prime number")
else:
    print(f"{n} is NOt git prime number")