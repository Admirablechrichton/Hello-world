import random
guessesTaken = 0
number = random.randint(1, 30)
while 4 > 2:
    guess = int(input('Take a guess :'))
    guessesTaken += 1
    if guess < number:
        print("your guess is too low")
    if guess > number:
        print("your guess is too high")
    if guess == number:
        print('congratulations, you guess right!👋👋👋👋👋👋👋')
        break
    else:
        if guessesTaken == 5:
            print('you have reached the guess limit, the correct number is:', number, 'Thanks for guessing.')
            break