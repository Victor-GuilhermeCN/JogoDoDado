from random import randint
# Draw the possible numbers of a common die.
dice1 = randint(1, 6)
dice2 = randint(1, 6)
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
            print(f'1º Dice:{dice1} 2º Dice:{dice2}')
        else:
            print('Ok, bye bye')

