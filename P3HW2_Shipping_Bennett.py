# CTI-110 
# P3HW2 - Shipping Charges 
# Forrest Bennett
# 09/27/18
#Write a program that asks the user to enter the number of packages purchased.
#The program should display the amount of the discount (if any) and the total
#amount of the purchase after the discount.

Pounds = float(input('Enter total weight of package in pounds.'))

shipping = 0

if Pounds <=2:
    shipping = Pounds * 1.50
elif Pounds <=6:
    shipping = Pounds * 3.00
elif Pounds <10:
    shipping = Pounds * 4.00
else:
    shipping = Pounds * 4.75
#Display Shipping Charges.
    
print('The shipping is', format(shipping, ',.2f'))

    
