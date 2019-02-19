def funOne(msg):
    print (msg)

funTwo = funOne 

#----------------------------------------------------------------------------------------------------------------------
#Passing a function as an argument to another function

#Example 1
def funThree(func,msg):
    return (func(msg))  #Try giving print instead and see the output



#Example 2
def inc(x):
    print (x+1)

def dec(x):
    print (x-1)

def operation(fun,x):
    return(fun(x))

#----------------------------------------------------------------------------------------------------------------------
#closures

def funFour(encod):
    def funFive(msg):
        print (encod(msg))
    return funFive

#first = funFour(oct)
#first(124)
#----------------------------------------------------------------------------------------------------------------------
#decorators
def funSix(func):
    def funSeven():
        print ("This is funSeven within funSix.")
        func()
    return funSeven #return the function and call it later, after creating the main function's object.
@funSix
def funEight():
    print ("This is funEight.")

funEight()
#----------------------------------------------------------------------------------------------------------------------
#decorator with arguments.
def divideDecorator(func): 
    def inner(a,b):
        print ("Dividing - %s and %s" %(a,b))
        if b == 0:
            print ("Whoops! b cannot be zero")
            return
        return (func(a,b))
    return inner

@divideDecorator
def divide(a,b):
    print (a/b)

# result = divideDecorator(divide)
# result(12,2)
divide(12,2)

#----------------------------------------------------------------------------------------------------------------------
def runningFun():
    funOne("This is function one.")
    funTwo("This is the same function object, but with a different name.")
    funThree(funOne,"This is function three accessing the first function.")
    operation(dec,12)

#runningFun()