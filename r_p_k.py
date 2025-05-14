import random
print("Lets play Rock Paper and Scissor")
print("Type 'r'-Rock,\n     'p'-Paper\n     's'-Scissor")
def r_p_s(user_choice):
    game = ['r', 'p', 's']
    computer = random.choice(game)
    if computer == user_choice:
        print(f'Computer( {computer} ) vs You( {user_choice} )')
        print("It's a tie. ")
    elif computer == 'r' and user_choice == 'p':
        print(f'Computer( {computer} ) vs You( {user_choice} )')
        print('You win.')
    elif computer == 'p' and user_choice == 'r':
        print(f'Computer( {computer} ) vs You( {user_choice} )')
        print('You loss.')
    elif computer == 's' and user_choice == 'r':
        print(f'Computer( {computer} ) vs You( {user_choice} )')
        print('You win.')
    elif computer == 'r' and user_choice == 's':
        print(f'Computer( {computer} ) vs You( {user_choice} )')
        print('You loss.')
    elif computer == 's' and user_choice == 'p':
        print(f'Computer( {computer} ) vs You( {user_choice} )')
        print('You loss.')
    elif computer == 'p' and user_choice == 's':
        print(f'Computer( {computer} ) vs You( {user_choice} )')
        print('You win.')
    else:
        print('Not a valid input')


while True:
    usr_c = input("Enter your choice: ")
    r_p_s(usr_c)
    inp = input('Do you want to play again..(y/n): ')
    if inp == 'y':
        pass
    else:
        break
