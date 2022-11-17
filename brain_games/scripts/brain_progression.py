import random
import prompt


welcoming = print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
hello = print(f"Hello, {name}!")
question = "What number is missing in the progression?"


def progression(num):
    start = random.randint(0, 10)
    counter = random.randint(1, 5)
    a = list(range(start, 20, counter))
    delete = random.randint(0,len(a)-1)
    check = a[delete]
    b = a.pop(delete)
    c = a.insert(delete, '..')
    resp = ''
    result = 0
    ans = prompt.string(f"Question: {a}\nYour answer: {resp}")
    if int(ans) == int(b):
        print("Correct!")
        result = 1
    if int(ans) != int(b):
        print(f"'{ans}' is wrong answer ;(. Correct answer was '{b}'.\nLet`s try again, {name}")
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
