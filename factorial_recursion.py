#this is factorial program
def factorial(n1):
    if n1 == 0: return 1
    else:
        return n1*factorial(n1-1)

print(factorial(5))
print(factorial(6))
