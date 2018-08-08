# Basic Collatz Sequence Program
# NeerajNair
# Chapter 3 


def collatz(num):
    if num % 2 == 0:
            evn_val = num // 2
            print(evn_val)
            return evn_val
    elif num % 2 == 1:
            odd_val = 3 * num + 1
            print(odd_val)
            return odd_val

print("***** Collatz Sequence Prog *****")
user_input = int(input("Enter an Input - Must be a Number   -->  "))
print("***Input Recieved, Printing The Collatz Sequence***")
while user_input != 1:
    user_input = collatz(int(user_input))





    
 

