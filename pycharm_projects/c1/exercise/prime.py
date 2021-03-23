if __name__ == '__main__':
    
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