print("Welcome To The Tip Calculator!")
total_bill = float (input("what was the total bill?\n $" ))
tip_in = float(input("how much tip would you like to give? 10,12 or 15? \n"))
no_people = int(input("how many people are spilting the bill? \n"))
x = int(tip_in)
tip = (x/100) * total_bill
payment = (total_bill +tip) / no_people
round_payment = round(payment,2)
print(f"Each person sould pay ${round_payment}")
