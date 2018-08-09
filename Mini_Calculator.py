

def add(val1,val2):
	ans = val1 + val2
	print("Answer = {}".format(ans))

def sub(val1,val2):
	ans = val1 - val2
	print("Answer = {}".format(ans))

def mul(val1,val2):
	ans = val1 * val2
	print("Answer = {}".format(ans))

def div(val1,val2):
	ans = val1 / val2
	print("Answer = {}".format(ans))

print("Hello Welcome to my Mini-Calculator Program")

name = raw_input("Please Enter your First Name  --  ")
print("Hello {}".format(name))

val1 = float(input("Enter Your First Number"))
val2 = float(input("Enter Your Second Number"))

print("Select 1 for Add")
print("Select 2 for Sub")
print("Select 3 for Mul")
print("Select 4 for Div")
	
# Loop starts here
user_choice = input("Please Enter a choice")
if user_choice == 1:
	 add(val1,val2)
elif user_choice == 2:
	 sub(val1,val2)
elif user_choice == 3:
	 mul(val1,val2)
elif user_choice == 4:
	 div(val1,val2)