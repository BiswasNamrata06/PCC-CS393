def digit_sum(n):
    while n >= 10:
        sum_digits = 0
        while n > 0:
            sum_digits += n % 10
            n //= 10
        n = sum_digits
    return n

num = int(input("Enter a number: "))

if digit_sum(num) == 1:
    print(f"{num} is a Magic Number!")
else:
    print(f"{num} is NOT a Magic Number.")
