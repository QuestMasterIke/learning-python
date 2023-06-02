#
# Example file for working with functions
# LinkedIn Learning Python course by Joe Marini
#


# TODO: define a basic function
def function():
    print("Hello from function      ")
    
function()

# TODO: function that takes arguments
def function2(zahl,z2):
    print(zahl+z2)

function2(4,5)

# TODO: function that returns a value
def cube(x):
    return x*x*x

print(cube(3))

# TODO: function with default value for an argument
def power(num,x=1):
    result=1
    for i in range(x):
        result=result*num
    return result

print(power(3))
# TODO: function with variable number of arguments

def multi_add(*args):
    result=0
    for x in args:
        result+=x
    return result


print(multi_add(2,6,9,5))

