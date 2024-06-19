# 1.4. Find numbers and sum of integers > 100 and < 200 divisible by 7

def find_numbers_divisible_by_7():
    numbers = [num for num in range(101, 200) if num % 7 == 0]
    sum_numbers = sum(numbers)
    return numbers, sum_numbers

numbers_divisible_by_7, sum_numbers = find_numbers_divisible_by_7()
print(f"Numbers divisible by 7 between 100 and 200: {numbers_divisible_by_7}")
print(f"Sum of these numbers: {sum_numbers}")


