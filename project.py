import random
number = random.randint(1, 10)


chances = 0


while chances < 5:
    guess = int(input("Enter Guess Here: "))
    chances += 1
    if guess < number:
        print('Your guess is too low')
    if guess > number:
        print('Your guess is too high')
    if guess == number:
        print('Congratualations! You guessed the number in ' + str(chances) + ' tries!')
        break
    if  chances > 5:
        print("YOU LOSE!!") 
        break
