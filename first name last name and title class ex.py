def name():
    input("Please enter your first name: ")


def last_name():
            input("Please enter your last name: ")
        
def title_name ():
    input ("Please enter your title e.g Mr Miss Mrs: ")
     
def get_data ():
    fname = name()
    lname = last_name()
    title = title_name()
    return title , fname , lname

def message (title , fname , lname):
    message = print("Welcome {0} {1} {2}".format(title , fname , lname))
    return message

def display(get_data , message):
    get_data()
    print (message)


display (get_data , message)


 
    
