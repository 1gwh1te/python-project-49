import random
import prompt


welcoming = print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
hello = print(f"Hello, {name}!")
question = "What number is missing in the progression?"


def progression(num):
    start = random.randint(0, 5)
    counter = random.randint(1, 4)
    a = list(range(start, 26, counter))
    delete = random.randint(0, len(a) - 1)
    b = a.pop(delete)
    a.insert(delete, '..')
    to_print = ' '.join(str(item) for item in a)
    resp = ''
    result = 0
    t = " is wrong answer ;(. Correct answer was "
    ans = prompt.string(f"Question: {to_print}\nYour answer: {resp}")
    if int(ans) == int(b):
        print("Correct!")
        result = 1
    if int(ans) != int(b):
        print(f"'{ans}'{t}'{b}'.\nLet's try again, \"{name}!")
        result = 2
    return result


def main():
    num = 1
    print(question)
    index = 1
    while index <= 3:
        result = progression(num)
        if result == 2:
            break
        if index == 3 and result == 1:
            print(f'Congratulations, {name}!')
            break
        index += 1


if __name__ == '__main__':
    main()
