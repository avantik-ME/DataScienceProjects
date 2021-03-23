if __name__ == '__main__':
    # ask for number 1 and 2
    x = int(input('Enter the first number: '))
    y = int(input('Enter the second number: '))

# divisibility test:
    if (x % y) == 0:
        print(f'{x} is divisible by {y}')

    elif (y % x) == 0:
        print(f'{y} is divisible by {x}')

    else:
        print('these numbers failed divisibility test')
