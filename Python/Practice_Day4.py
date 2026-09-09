# Read File///////////////////////////////////////////////////////////////////////////////////////////////////////////////

# f = open("t.txt", "a")
# data = f.read()
# print(data)
# f.close()

# Write File  ============================================================================================================

# f = open("t.txt", "a")
# data = f.write("Hi i am mangesh and you")
# print(data)
# f.close()

# with open("t.txt", "r") as f:
#     data =f.read()
#     print(data)
#     f.close()

# import os

# os.remove("t.txt")

# f = open("t.txt", "w+")
# data = f.write('''Hi everyone
# we are learning File I/O
# using Java.
# I like programming in Java.''')
# print(data)
# f.close()

# Object oriented Programming (OOP)==================================================================

# Class & Object in Python ===================================

# class classroom:
#     s1 = "mangesh"
#     s2 = "shubham"
#     s3 = "atul"

# student = classroom()
# print(student.s1)

# class student:
#     def __init__(self, name):
#         self.name = name

# s1 = student("mangesh")
# print(s1.name)

# class student:
#     def __init__(self, name, marks):
#         self.name = name
#         self.marks = marks

#     def get_avg(self):
#         sum = 0 
#         l = len(self.marks)
#         for mark in self.marks:
#             sum+= mark
#         print("Hi,", self.name, "your avg is", sum/l)


# s1 = student("mangesh", [95, 85, 84])
