#get number
def get_num():
    number = int(input("Please enter a ODD NUMBER to make the pattern: "))
    return number


#get the odd number
def odd_number(number):
    
    if number %2==0:
        tf = False
    return tf
#
def numberloop (tf ,number):
    tf = True 

    while tf != True:
        get_number (number)
    

#CALCULATE THE PYRAMID
def pyramid (number):
    while number != 1:
        newnumber = number - 1

        message =(newnumber * string)
        return message



number = 0
tf = 0
string = "*"
number  = odd_number (number)
get_num() 
numberloop(tf,number)
message = pyramid(number)
print (message)
