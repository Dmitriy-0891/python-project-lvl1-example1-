#!:/usr/bin/env python3

import prompt
import random


def main():
    num_1 = random.randint(1, 1000)
    num_2 = random.randint(1, 1000)
    print(f"Question: {num_1} {num_2}")
    answer = prompt.string('Your answer: ')
    pgcd = 1
    gcd = 1
    if num_1 > num_2:
        # possible greatest common divisor
        pgcd = num_2
    else:
        pgcd = num_1

    for i in range(pgcd, 1, -1):
        if num_1 % i == 0:
            if num_2 % i == 0:
                # greatest common divisor
                gcd = i
                break
    if answer == str(gcd):
        return True
    else:
        print(f"'{answer}' is wrong answer:(. Correct answer is {gcd}.")
        return False


if __name__ == '__main__':
    main()