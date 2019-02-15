def function_creator(): 
  
    # expression to be evaluated 
    expr = raw_input("Enter the function(in terms of x):") 
  
    # variable used in expression 
    x = int(raw_input("Enter the value of x:")) 
  
    # evaluating expression 
    y = eval(expr) 
  
    # printing evaluated result 
    print("y = {}".format(y))
    
#function_creator()

def add(*args):
    n=0
    for i in args:
        n += i
    return n  
#print (add(1,2,3,4))

def multiply(*args):
    n=1
    for i in args:
        n *= i
    return n
mul = [1,2,3,4,5]
print (multiply(*mul))
    
