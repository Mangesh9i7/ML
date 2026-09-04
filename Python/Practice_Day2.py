# List, Tupel, Set and Dictionary Practice questions
# numbers = [55, 69, 64, 68, 39]
# print("First element:", numbers[0])
# print("Last element:", numbers[-1])
# print("Length:", len(numbers))
# print("Maximum:", max(numbers))
# print("Minimum:", min(numbers))


# cities = ("Pune", "Mumbai", "Delhi", "Chennai", "Bangalore")
# print(cities[1])
# print(cities[4])

student_data = {}
name = input("Enter your full name:- ")
age = int(input("Enter your age:- "))
student_data["name"] = name
student_data["age"] = age

student_data["subjects"] = {
    "Phy": float(input("Enter your Phy marks: ")),
    "Math": float(input("Enter your Math marks: ")),
    "Bio": float(input("Enter your Bio marks: "))
}

p = student_data["subjects"]["Phy"]
m = student_data["subjects"]["Math"]
b = student_data["subjects"]["Bio"]
avg = (p + m + b) / 3

if avg > 90:
    print("Excellent")
elif avg > 75 and avg < 90:
    print("Very Good")
elif avg > 50 and avg < 75:
    print("Pass")
else:
    print("Fail")

print("\nStudent Information:")
print(student_data)