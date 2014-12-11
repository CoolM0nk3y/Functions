# get the tempture in Fahrenheit
def Fahrenheit ():
    fahrenheit = int(input("Please enter the tempture in Fahrenheit: "))
    return fahrenheit

def calculate(fahrenheit):
    celsius = (fahrenheit - 32) * (5/9)
    Celsius = round(celsius,2)
    return Celsius 





#main program
fahrenheit = Fahrenheit ()
Celsius  = calculate(fahrenheit)
print(" The conversion says that the tempture you enterd in Fahrenheit is {0} Celsuius".format(Celsius ))
