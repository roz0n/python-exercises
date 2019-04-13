digits = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# for digit in digits:
#    print(digit**2)

# for digit in digits:
#    print(digit > 5)

for digit in digits:
    if digit > 5:
        print("{} is greater than five!".format(digit))
    elif digit == 5:
        print("{} is equal to five.".format(digit))
    else:
        print("{} is less than five...".format(digit))
