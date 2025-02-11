def is_prime(num) -> bool:

    if num >= 2:
        i=2
        while i< int(num ** 0.5)+1 :
            if num % i ==0:
                return False
        i = i + 1
    else:
        return False
    return True

n = int(input("Input number : "))
if is_prime(n):
    print(f"{n} is prime number")
else:
    print(f"{n} is NOT prime number!")

