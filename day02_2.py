#v1.1) for -> while
#v1.2) while 구문으로 구간 소수를 출력하는 프로그램
#v1.3) ** 대신 pow 함수를 사용


def is_prime(num) -> bool:
    """
    A function prime number true or false
    :param num:
    :return:
    """
    if num >=2:
        for i in range(2, int(num ** 0.5) + 1):
            if num % i==0:
                return False
    else:
        return False
    return True

#main
    help(is_prime)
    n = int(input("Input number : "))

    if is_prime(n):
        print(f"{n} is prime number")
    else:
        print(f"{n} is NOT prime number!")



