import math

mort = int(input("Please enter how much your mortgage is: "))
inter = float(input("Please enter how much your interest rate is: "))
length = int(input("Last question, How many years is your mortgage? Usually they are 15 or 30 years. "))

def totalamount(x,y):
	total = x * y
	print("The total amount of your mortgage is {}".format(total))
	return total

print(mort)
print(inter)

total_amount = totalamount(mort,inter)

def yearly(length):
	year = (total_amount/length)
	yearRound = round(year,2)
	print("Every year you are going to pay {} in mortgage payments.".format(yearRound))
	month = (year/12)
	monthRound = round(month,2)
	print("Every month you are going to pay {} in mortgage payments.".format(monthRound))

yearly(length)


