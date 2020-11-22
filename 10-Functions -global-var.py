x = 6

def example():
    global x
    print (x)
    # This command can be run because the var was defined as a global var
    x+=5
    print(x)

example()


# In the following example globx is a local var and we can access globx just from the function (not outside)
def example1():
    globx = x
    print(globx)
    globx+=5
    print(globx)
    # The solution for the private situation
    return globx 


x = example1()
print (x)


def doubleIt(x):
    # return 2*x is the same
    return x+x

x = doubleIt(4)

print (x)

print (doubleIt(4))



def doubleIt1(x):
    if x > 5:
        return "cat"
    else:
        return "dog"

print (doubleIt1(4))
