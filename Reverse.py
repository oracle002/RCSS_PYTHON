# 1.6. Reverse digits of a number and check if it's a palindrome

def reverse_digits_and_check_palindrome(number):
    original = number
    while True:
        reverse = int(str(number)[::-1])
        number += reverse
        if str(number) == str(number)[::-1]:
            return number

number = int(input("Enter a Number:  "))
result = reverse_digits_and_check_palindrome(number)
print(f"Final palindrome number after reversing and adding: {result}")


