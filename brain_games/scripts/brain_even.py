import prompt
import random

print("Welcome to the Brain Games!")
name = prompt.string('May I have your name? ')

def is_even(num):
    if num % 2 == 0:
        return True
    else:
        return False

def question(num):
    response = ''
    result = 0
    num = random.randint(0, 100)
    answer = prompt.string(f'Question: {num}\nYour answer: {response}')
    if answer != 'yes' and answer != 'no':
        print(f"\{answer}\" is wrong answer ;(\nLet's try again, {name}!")
        result = 3
    if is_even(num) == True and answer == 'yes':
        print('Correct!')
        result = 1
    if is_even(num) == False and answer == 'no':
        print('Correct!')
        result = 1
    if is_even(num) == True and answer == 'no':
        print(f"\"no\" is wrong answer ;(. Correct answer was \'yes\'\nLet's try again, {name}!")
        result = 3
    if is_even(num) == False and answer == 'yes':
        print(f"\"yes\" is wrong answer ;(. Correct answer was \'no\'\nLet's try again, {name}!")
        result = 4
    return result
def main():
    index = 1
    print(f'Hello, {name}!')
    print(f"Answer \"yes\" if the number is even, otherwise answer \"no\"")
    while index <= 3:
        result = question(index)
        if result == 3 or result == 4:
            break
        if index == 3 and result == 1 :
            print(f'Congratulations, {name}')
            break
        index += 1
if __name__ == '__main__':
    main()
