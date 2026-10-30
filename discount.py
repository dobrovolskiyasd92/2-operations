price_product = float(input('Price product: '))
discount = int(input('Percent of discount: '))

print(f'Your price with discount: {(price_product * (100-discount)/100):.2f}')

