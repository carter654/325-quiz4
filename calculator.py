def add():
	print("\n" * 500)
	print("you choose addition\n\n")
	num1 = input("Please enter first number: ")
	num2 = input("Please enter second number: ")
	output = float(num1) + float(num2)
	print("\n" * 500)
	print(f"Your answer is {num1} + {num2} = {output}")
	input("\nPress Enter to continue...")








while True:
	print("\n" * 500)
	print("=========SIMPLE CALCULATOR PROGRAM=========\n")

	print("\nEnter:\n    1 for addition\n    2 for subtraction\n    3 for multiplication\n    4 for division\n    0 to exit\n\n")

	option = input("===========================================\nintput: ")



	if option == "0":
		print("\n" * 500)
		exit(0)


	elif option == "1":
		add()



