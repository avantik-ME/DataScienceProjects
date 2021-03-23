if __name__ == '__main__':
    # ask for number 1 and 2
    X_string = input('Enter a list of five single digit separated by space')
    y = int(input('Enter a single digit number: '))

    List = X_string.split()
    print("num list is ", List)

    for i in List:
        for n in List:
            if (int(i) + int(n)) == y:
                print(f'{i},{n}')

            else:
                print(f'{i},{n} do not add up to {y}')

