# 1. Arithmetic Operators
# 2. Assignment Operators
# 3. Comparison Operators
# 4. Logical Operators
# 5. Bitwise Operators
# 6. Special Operators


# 1. Arithmetic Operator

a = 20
b = 10
c = 3

print("\n\nAssignment Operator")
#    Addition +
print("Addition = ", a+b)

#    Subtraction -
print("Subtraction = ", a-b)

#    Multiplaction *
print("Multiplaction = ", a*b)

#    Division / 
print("DIvision = ", a/c) # division is gives the float value as a answer

#    Floor Division //
print("Floor Division = ", a//c) # floor division is gives the int value as a answer

#    Modulo %
print("Modulo = ", a%c)

#    Power **
print("Power = ", a**c)

# 2. Comparison Operators

print("\n\nComparison Operators")
# Is Equal To
print("3 == 2 ", 3==2)
print("2 == 2 ", 2==2)
# Not Equal To
print("3 != 2", 3!=2)
print("2 != 2 ", 2!=2)
# Greater Than
print("3 > 2", 3>2)
print("2 > 3",2>3)
# Less Than
print("3 < 2",3<2)
print("2 < 3",2<3)
# Greater Than or Equal
print("3 >= 2", 3>=2)
print("2 >= 2", 2>=2)
print("2 >= 3",2>=3)
# Less Than or Equal To
print("3 <= 2", 3<=2)
print("2 <= 2", 2<=2)
print("2 <= 3",2<=3)

# 3. Logical Operators

print("\n\nlogical operators")
# logical and (if all conditions are true than gives true otherwise gives false)
print("3 > 2 and 4 > 1", (3>2 and 4>1))
print("3 > 2 and 2 > 3", (3>2 and 2>3))

# logical or (if any one condition are true than gives the true)
print("3 > 2 or 4 > 1 ", (3>2 or 4>1))
print("3 > 2 or 2 > 3 ", (3>2 or 2>3))
print("2 > 3 or 1 > 4 ", (2>3 or 1>4))

# logical   not (it gives the opposite value)
print("not 3 > 2 ", not 3>2)
print("not 2 > 3 ", not 2>3)


# 4. Assingnment Operator

print("\n\nAssignment Operator")
# Assignment Operator
no = 10
print("No = ", no)
# Addition Assignment
no+=1 # no = no + 1
print("No+=  ", no)
# Subtraction Assignment
no-=1 # no = no - 1
print("No-=  ", no)
# Multiplication Assignment
no*=2 # no = no * 2
print("No*=  ", no)
# Division Assignment
no/=2 # no = no / 2
print("No/= ", no)
# Remainder Assignment
no%=2 # no = no % 2
print("No%= ", no)
# Exponent Assignment
no**=2 # no = no ** 2
print("No**= ", no)

# 5. Special operators

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

print("\n\nSpecial Operators")
# is (True if the operands are identical (refer to the same object))
print("x1 is y1 = ",x1 is y1)
print("x2 is y2 = ",x2 is y2)
print("x3 is y2 = ",x3 is y3)
# is not (True if the operands are not identical (do not refer to the same object))
print("x1 is not y1 ",x1 is not y1)
print("x2 is not y2 ",x2 is not y2)
print("x3 is not y3 ",x3 is not y3)