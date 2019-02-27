#calculate the factorial of a positive integer


def factorial(n):
    if n == 0:                      #base condition
        return 1
    else:
        return n * factorial(n-1)   #cursive condition

print(factorial(6))
