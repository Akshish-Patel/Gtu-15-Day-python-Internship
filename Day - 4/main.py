# python module is the file which file contains the some ffunction and other details which can use by us in our working file
import module
import fuunction as f

print("greet() function from module")
module.greet("Ram")

print("\n\nprintTable() function from module")
module.printTable(4)


print("\n\nmark of sudents from module")
print(f"Marke of Student object is {module.student['marks']}")


print("\n\nAddition function from module")
no1 = int(input("Enter the no1 : "))
no2 = int(input("Enter the no2 : "))
print(f"Addition of {no1} and {no2} is {module.addition(no1, no2)}")

print("\n\division() function from functiion module or library")
no1 = int(input("Enter the no1 : "))
no2 = int(input("Enter the no2 : "))
print(f"Division of {no1} and {no2} is {f.division(no1, no2)}")