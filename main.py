import random


def main():
    total = 0
    numbers = []
    
    """
    ########################################
    Code Your Program here
    ########################################
    """

    while total <= 100:
        random_numbers = random.randint(0,100)
        if total + random_numbers > 100:
            break
        numbers.append(random_numbers)
        total += random_numbers
    numbers.append(random_numbers)
        

    print(f'The random values are {numbers}, {random_numbers}')
    print(f'The total is {total}')

    ########################################
    # Do not delete the return statement
    ########################################
    return numbers, total


if __name__ == '__main__':
    main()
