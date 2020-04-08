from random import randint
# Draw the possible numbers of a common die.
# Create Lines
def line():
    print('-' * 50)

# Structure the title by centralizing it.
def title(msg):
    line()
    print(msg.center(50))
    line()

# Asks if you want to roll the dice.
def wannaplay():
    try:
        option = str(input('Would you like to roll the dice? [Y/N]:')).upper().strip()[0]
    except:
        print('You entered an incorrect option... Try again.')
        return wannaplay()
    else:
        # Checks whether the answer is Y or N.
        while option not in 'YN':
            print('You entered an incorrect option... Try again.')
            return wannaplay()
        if option == 'Y':
            # Draw the possible numbers of a common dice.
            print(f'1º Dice:{randint(1, 6)} 2º Dice:{randint(1, 6)}')
            return wannacontinous()
        else:
            print('Ok, bye bye')

def wannacontinous():
    try:
        answer = str(input('Do you wanna roll the dice again? [Y/N]:')).upper().strip()[0]
    except:
        print('You entered an incorrect option... Try again.')
    else:
        while answer not in 'YN':
            print('You entered an incorrect option... Try again.')
            return wannacontinous()
        if answer == 'Y':
            return wannaplay()
        else:
            while True:
                print('Ok, bye, bye.')
                break