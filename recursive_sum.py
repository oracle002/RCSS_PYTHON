# 1.5. Recursive function to calculate sum of numbers from 0 to 10

def recursive_sum(n):
    if n == 0:
        return 0
    else:
        return n + recursive_sum(n - 1)

result = recursive_sum(10)
print(f"Sum of numbers from 0 to 10 is: {result}")


