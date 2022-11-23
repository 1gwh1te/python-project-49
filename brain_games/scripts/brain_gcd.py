import prompt
import random


welcoming = print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')
hello = print(f'Hello, {name}!')
question = "Find the greatest common divisor of given numbers."


def find_nod(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    result = (a + b)
    return result


def nod(num):
    n1 = random.randint(0, 10)
    n2 = random.randint(0, 10)
    res = find_nod(n1, n2)
    resp = ''
    result = 0
    t = f" is wrong answer ;(. Correct answer was '{res}'.\nLet`s try again, "
    ans = prompt.string(f'Question: {n1} {n2}\nYour answer: {resp}')
    if int(ans) == find_nod(n1, n2):
        print('Correct!')
        result = 1
    if int(ans) != find_nod(n1, n2):
        print(f"{ans}{t}{name}!")
        result = 2
    return result


def main():
    print(question)
    index = 1
    while index <= 3:
        result = nod(index)
        if result == 2:
            break
        if index == 3 and result == 1:
            print(f'Congratulations, {name}!')
            break
        index += 1


if __name__ == '__main__':
    main()
