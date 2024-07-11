# Lambda Function

# lambda function is the way to define a function wiht the help of lambda key word insted of def key word
# syntex of lambda function : lambda arguments : body

greet = lambda : print("Good mornign!!")

greet()

print("\nCalling of add function")
add = lambda x, y : print(f"Addition of {x} and {y} is {x+y}")
add(5,3)

print("\nCalling of cube function")
cube = lambda x : pow(x,3)
print("Power of 6 is ", cube(6))

def func(fx, no):

    return fx(no)+no

print("\nfunc = ", func(cube, 6)) #we can direct pass the function as a argument
print("\nfunc = ", func(lambda x : x*x*x, 6))# we can pass the function as a argument with help of lambda
