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
    for i in range(number-1):
        numwhite = number-i
        message = print (' '*numwhite + '*'*i + '*'*i)
    return message 



number = 0
tf = 0
number  = odd_number (number)
get_num() 
message = " "
print (message)
