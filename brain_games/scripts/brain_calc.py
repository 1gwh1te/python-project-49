import prompt
import random

welcoming = print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
hello = print(f'Hello, {name}!')
question = "What is the result of the expression?"


def calc(num1):
    resp = ''
    res = 0
    check = 0
    ops = ['+', '-', '*']
    op = random.choice(ops)
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    ans = prompt.string(f'Question: {n1} {op} {n2}\nYour answer: {resp}')
    if op == '+':
        res = n1 + n2
    if op == '-':
        res = n1 - n2
    if op == '*':
        res = n1 * n2
    if int(ans) == res:
        print('Correct!')
        check = 1
    if int(ans) != res:
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{res}'.\nLet`s try again, {name}!")
        check = 2
    return check


def main():
    print(question)
    index = 1
    while index <= 3:
        result = calc(index)
        if result == 2:
            break
        if index == 3 and result == 1:
            print(f'Congratulations, {name}!')
            break
        index += 1


if __name__ == '__main__':
    main()
