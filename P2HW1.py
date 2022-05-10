# A brief description of the project
# 02/26/2022
# CTI-110 P2HW1 - Total Purchases
# Andre Allen Jr
print('Enter the price of Item 1')
Item1 = float(input())
print('Enter the price of Item 2')
Item2 = float(input())
print('Enter the price of Item 3')
Item3 = float(input())
print('Enter the price of Item 4')
Item4 = float(input())
print('Enter the price of Item 5')
Item5 = float(input())
Subtotal =Item1 + Item2 + Item3 + Item4 + Item5
Tax = Subtotal * 0.07
Total = Subtotal + Tax
print('-----Results-----')
print('Subtotal: {0:.2f}'.format(Subtotal))
print('Tax: {0:.2f}'.format (Tax))
print('Total: {0:.2f}'.format (Total))

#Display "Enter the price for Item 1"
#Input Item1
#Display "Enter the price for Item 2"
#Input Item2
#Display "Enter the price for Item 3"
#Input Item3
#Display "Enter the price for Item 4"
#Input Item4
#Display "Enter the price for Item 5"
#Input Item5
#Set Subtotal = Item1 + Item2 + Item3 + Item4 + Item5
#Set Tax = Subtotal * 0.07
# Set Total = Subtotal + Tax
#Display "Subtotal: ", Subtotal
#Display "Tax: ", Tax
#Display "Total: ", Total