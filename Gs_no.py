
import random

random_num = random.randrange(51)
print("Guess the number between 0 to 50.....\n")
def guess(users_guess):
    if int(users_guess) == random_num:
        print("Congratulation!!! you have guessed the right Number.")
        return False
    elif int(users_guess) < random_num:
        print(f"It is greater than {users_guess}.\nTry again")
        return True
    elif int(users_guess) > random_num:
        print(f'It is smaller than {users_guess}.\nTry again')
        return True

while True:
    pred=input("Predict a number: ")
    if guess(pred) == True:
        pass
    else:
        break



