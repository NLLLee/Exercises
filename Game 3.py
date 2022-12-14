print("welcome to the tip calculate!")
bill = float(input("what was the total bill?"))
tip = int(input("how much tip would you like to give? 10, 12, or 15"))
people = int(input("how many people to splist the bill"))

bill_with_tip = tip / 100 *bill + bill
each_person_pay = bill_with_tip / people
final_amount = round(each_person_pay, 2)
final_amount = "{:.2f}".format(each_person_pay)
print(f"each person should pay ${final_amount}")