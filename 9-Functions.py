def example():
    print('basic function')
    z = 3+9
    print(z)


example()

def simple_addition(num1,num2):
    answer = num1 + num2
    print('num1 is ',num1)
    print(answer)

simple_addition(3,5)
simple_addition(num2=3,num1=5)


def simple(num1,num2):
    pass

# Make a default parameter
def simple(num1,num2=5,num3=2):
    print(num1,num2,num3)

simple(2,num3=1)
simple(2)



