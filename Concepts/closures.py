#closure
def funOne():
    print ("Hello!")
    def funTwo():
        print ("How are you?")
    return funTwo                   #Without using closures - return funTwo()
call = funOne()                     #Without using closures - funOne()
call()

def c_temp(x,y):
    print ("%fC" %(x+y/2))
    def f_temp():
        c = (x+y)/2
        print ("%fF"%((c*9/5)+32))
    return f_temp
to_f = c_temp(12.55,15.61)
to_f2 = c_temp(37.5,36.6)

to_f()
