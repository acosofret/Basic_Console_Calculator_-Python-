from replit import clear
from art import logo


def add(n1, n2):
	return n1 + n2


def subtract(n1, n2):
	return n1 - n2


def multiply(n1, n2):
	return n1 * n2


def divide(n1, n2):
	return n1 / n2


operations = {"+": add, "-": subtract, "*": multiply, "/": divide, }


# we're defining a function for the entire program,
# so it can be called back from the beginning
# when the user is finishing with current calculation
def calculator():
	print(logo)
	# choose the 1st number:
	num1 = float(input("What's the first number?: "))
	clear()
	# choose the operator(from a shown list):
	for symbol in operations:
		print(symbol)
	operation_symbol = input("Now pick an operation from the list above: ")
	clear()
	# choose the 2nd number:
	num2 = float(input("What's the second number?: "))
	clear()
	# perform the desired calculation:
	if operation_symbol in operations:
		calculation = operations[operation_symbol]
		result = calculation(num1, num2)
		print(f"{num1} {operation_symbol} {num2} = {result}")

		# ask if they want to continue with further calculations:
	further = str.lower(input(f"\nContinue calculating with {result}?\nType 'y' or 'n'.\n"))
	clear()
	while further == "y":
		# ask for the new operation:
		for symbol in operations:
			print(symbol)
		operation_symbol = input("Pick another operation:")
		clear()
		# ask for the new number:
		num3 = float(input("And a new number please. "))
		clear()
		# perform new calculation
		if operation_symbol in operations:
			calculation = operations[operation_symbol]
			result2 = calculation(result, num3)
			print(f"{result} {operation_symbol} {num3} = {result2}\n\n\n")
			result = result2
		# ask if they want to continue with further calculations:
		further = str.lower(input(f"\nContinue calculating with {result2}?\nType 'y' or 'n'.\n"))
		clear()
	# exit loop, bye bye
	if further == "n":
		clear()
		print("Thanks for using our Calculator!")
		clear()
		print("See you next time.")
		clear()
		calculator()


calculator()
