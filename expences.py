food = int(input('How much money did you spend on food? '))
transport = int(input('How much money did you spend on transport? '))
entertainments = int(input('How much money did you spend on entertainments? '))

print(f'Total spent: {food + transport + entertainments}')
print(f'Average expense: {((food + transport + entertainments) / 3):.2f}')