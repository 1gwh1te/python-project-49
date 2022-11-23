import random
import prompt


welcoming = print("Welcome to the Brain Games!")
name = prompt.string("May I have your name? ")
hello = print(f"Hello, {name}!")
question = "Answer \"yes\" if given number is prime. Otherwise answer \"no\"."


def is_prime(num):
    result = False
    if num > 1:
        for i in range(2, num):
            if (num % i) == 0:
                result = True
                break
        if result == True:
            return False
        else:
            return True


def check(num):
    result = 0
    resp = ''
    num = random.randint(1, 100)
    ans = prompt.string(f"Question: {num}\nYour answer: {resp}")
    if ans == 'yes' and is_prime(num) == True:
        print("Correct!")
        result = 1
    if ans == 'no' and is_prime(num) == False:
        print("Correct!")
        result = 1
    if ans == 'yes' and is_prime(num) == False:
        print(f"'{ans}' is wrong answer ;(. Correct answer was 'no'.\nLet`s try again, {name}")
        result = 2
    if ans == 'no' and is_prime(num) == True:
        print(f"'{ans}' is wrong answer ;(. Correct answer was 'yes'.\nLet`s try again, {name}")
        result = 2
    return result


def main():
    num = 1
    print(question)
    index = 1
    while index <= 3:
        result = check(num)
        if result == 2:
            break
        if index == 3 and result == 1:
            print(f'Congratulations, {name}!')
            break
        index += 1


if __name__ == '__main__':
    main()

