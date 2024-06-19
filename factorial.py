# 1.8. Function to find factorial and store in a dictionary

factorials_dict = {}

def factorial(n):
    if n in factorials_dict:
        return factorials_dict[n]
    if n == 0:
        return 1
    else:
        result = n * factorial(n - 1)
        factorials_dict[n] = result
        return result

num = 5
print(f"Factorial of {num}: {factorial(num)}")
print("Factorials stored in dictionary:", factorials_dict)


