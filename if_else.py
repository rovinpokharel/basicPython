from __future__ import print_function
age = int(input("Please Enter your age: "))
if (age<=19):
	print("not allowed to drink")
else:
	print("allowed to drink")

name = input("What is your name?")
if name == "Rovin":
	print("Hello Rovin")
elif name == "Biraj":
	print("Hello Biraj")
else:
	print("I dont know who you are")

n = int(input("Please enter any integer"))
if n >= 0:
	if n == 0:
		print("Zero")
	else:
		print("+ve number")
else:
	print("-ve number")