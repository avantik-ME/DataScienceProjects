# This is a sample Python script.

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    #print_hi('PyCharm')
    num = int(input('Enter a number to check if it is a prime number: '))
    if num > 1:
        is_prime = True
        for j in range(2, (num // 2)+1):
            if (num % j) == 0:
                is_prime = False
                break

        if is_prime:
            print('number is a prime number')
        else:
            print('number is not a prime number')
    else:
        print('number is not a prime number')

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
