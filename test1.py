from sys import float_info

# Simple Calculator
num = int(input())

if num < 10000:
    print('This is a small number.')
else:
    digit1 = num%10
    num = num//10
    digit2 = num%10
    num = num//10
    digit3 = num%10


    sum = digit1+digit2+digit3

    if sum % 2 != 0:
        print("This is a great number")
    else:
        is_digit1_odd = digit1 % 2 != 0
        is_digit2_odd = digit2 % 2 != 0
        is_digit3_odd = digit3 % 2 != 0

        if is_digit1_odd or is_digit2_odd or is_digit3_odd:
            print("This is a good number")
        else:
            print("This is a bad number")




















