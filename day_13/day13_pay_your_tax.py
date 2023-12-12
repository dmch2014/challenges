# Write a function called your_vat. The function takes no
# parameter. The function asks the user to input the price of an
# item and VAT (vat should be a percentage). The function should
# return the price of the item plus VAT. If the price is 220 and,
# VAT is 15% your code should return a vat inclusive price of 253.
# Make sure that your code can handle ValueError. Ensure the
# code runs until valid numbers are entered. (hint: Your code
# should include a while loop).

import emojis
def pay_your_tax():
    while True:
        try:
            item = float(input("Tell me your item price:"))
            vat = float(input("% of VAT:"))
            item_vat_price = item + (item * (vat/100))
            print(item_vat_price)
            break
        except ValueError as ve:
            print(f'You entered {item} or {vat}, are not numbers.')


# Extra Challenge: Pyramid of Snakes
# Write a function called Python_snakes that takes a number
# as an argument and creates the following shape, using the
# number’s range: (hint: Use the loops and emoji library. If you
# pass 7 as argument, your code should print the following:
def python_snakes(number):
    for n in range(number):
        #print(emojis.encode(':snake:') * n)
        row_spaces = ' '*(number-n-1)
        print(row_spaces + emojis.encode(':snake:')*(n+1))






