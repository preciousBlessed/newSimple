#To create an iterator and use it to evaluate some number factorial

n = int(input("You wish to evaluate the factorial of ?: "))

def factorial_of_(n):
    if n == 0:
        print(f"{n}! = 1")
        return 0
    prod = 1
    def my_generator(n):
        for i in range(1, n+1):
            yield i

    for v in my_generator(n):
        prod *= v

    print(f"{n}! = {prod}")
    return prod


factorial_of_(n)