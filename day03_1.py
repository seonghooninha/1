import math

def my_pow(b, e) -> float:
    if e < 0:
        b=1/b
        e = e *-1

    result = 1
    i = int(e)
    f = e - i
    for _ in range(e):
        result = result * b

    if f > 0:
        result = result * math.exp(f*math.log(b))

    return result

print(my_pow(2, 9))
print(math.log(9))