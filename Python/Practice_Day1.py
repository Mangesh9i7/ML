# Variables, Operators, Data Types, Inputs(), and Conditional Statements Practis questions

# Question 1 
# Cheak if the number is Positive, Negative or Zero
# num = int(input("Inter a Number :"))

# if num > 0:
#     print("Number is Positive")
# elif num < 0:
#     print("Number is Negative")
# else:
#     print("Number is Zero")
# =========================================================================================================

# Question 2 
# Divisibility Checker :
# Take a number and check whether it is divisible by:
# 3
# 5
# both 3 and 5
# neither
# num = int(input("Enter a number: "))

# if num % 3 == 0 and num % 5 == 0:
#     print(num, "is divisible by both 3 and 5")
# elif num % 3 == 0:
#     print(num, "is divisible by 3")
# elif num % 5 == 0:
#     print(num, "is divisible by 5")
# else:
#     print(num, "is neither divisible by 3 nor 5")
# ===========================================================================================================

# Question 3 : Mini ATM Menu
Balance = 10000

print("Choose an option")
print("A : Check Account Balance")
print("B : Deposit Money")
print("C : Withdraw Money")
print("E : Exit")

Option = input("Enter your choice (A/B/C/E): ").upper()

if Option == "A":
    print("Your Balance is:", Balance)

elif Option == "B":
    amount = int(input("Enter your amount to deposit: "))
    Balance = Balance + amount
    print("Updated Balance:", Balance)

elif Option == "C":
    amount = int(input("Enter your amount to withdraw: "))
    if amount <= Balance:
        Balance = Balance - amount
        print("Updated Balance:", Balance)
    else:
        print("Insufficient funds!")

elif Option == "E":
    print("Goodbye!")

else:
    print("Invalid choice, please try again.")

