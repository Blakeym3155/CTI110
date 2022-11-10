# The brakdown of travel expenses for a trip
# 10/25/22
# CTI-110 P2HW1 - Travel
# Mikayla Blakey
#
#****************************Pseduocode***************************
#Display "This program calculates and displays travel expenses"
#Display "Enter Budget:"
#Input budget
#Display "Enter your travel destination:
#Input destination
#Display "How much do you think you will spend on gas?"
#Input gas price
#Display "Approxiamately, how much do you need for accomodation/hotel?"
#Input hotel price
#Display "Last, how much do you need for food?"
#Input food price
#Display "-------------Travel Expenses-------------"
#Display "Location:", destination
#Display "Inital Budget:" , budget
#Display "Fuel:" , gas price
#Display "Accomodation:" , hotel price
#Display "Food:" , food price
#Set total expenses = gas price + hotel price + food price
#Set remaining = budget - total expenses
#Display "Remaining balance:" , remaining


print('This program calculates and displays travel expenses')

budget = float(input('Enter Budget: '))
desination =(input('Enter your travel destination: '))
gas_price = float(input('How much do you think you will spend on gas? '))
hotel_price = float(input('Approciamately, how much do you need for accomodation/hotel? '))
food_price = float(input('Last, how much do you need for food? '))
print('------------------Travel Expenses--------------------')
total_expenses = food_price + gas_price +hotel_price
remaining = budget - total_expenses
print('location: ', '      ', desination)
print('Inital Budget:','      ','${}'.format(budget))
print('Fuel: ','      ','${}'.format(gas_price))
print('Accomodation: ','      ','${}'.format(hotel_price))
print('Food:','      ','${}'.format(food_price))
print('Remaining Balance: ','      ','${}'.format(remaining))
