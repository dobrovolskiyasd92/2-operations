food = int(input('How much money did you spend on food? '))
transport = int(input('How much money did you spend on transport? '))
entertainment = int(input('How much money did you spend on entertainments? '))

print(f'Total spent: {food + transport + entertainment}')
print(f'Average expense: {((food + transport + entertainment) / 3):.2f}')