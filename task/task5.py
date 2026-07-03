print("Welcome To The Tip Calculator!")
bill = float(input("What is Your total Bill?"))
tip_percentage_input = int(input("How much tip would you like to give? (e.g., 10, 12, 15)?"))
people = int(input("How many people to split the bill?"))
tip_as_decimal = tip_percentage_input / 100
total_bill_with_tip =tip_as_decimal * bill + bill
bill_per_person= total_bill_with_tip / people
final_amount = round(bill_per_person,2)
print(f"Each person should pay: ${final_amount}")