#Return the factorial of the provided integer. For example: 5! = 1 * 2 * 3 * 4 * 5 = 120

def factorialize(x):
    a = 1
    while x > 0:
        a = a * x
        x -= 1
    return a

print factorialize(5)
