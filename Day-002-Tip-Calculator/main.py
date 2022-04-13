print('Welcome to the tip calculator!')
total_bill = float(input('What was the total bill? $'))
tip_percentage = int(
    input('How much tip would you like to give? 10, 12, or 15? '))
number_of_people = int(input('How many people to split the bill? '))

each_person = (total_bill * (1 + (tip_percentage / 100))) / number_of_people

each_person = round(each_person, 2)

print(f'Each person should pay: ${each_person:.2f}\n')
