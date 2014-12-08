def name():
    fname = input("Please enter your first name: ")
    return fname


def last_name():
    lname = input("Please enter your last name: ")
    return lname
        
def title_name ():
    title = input ("Please enter your title e.g Mr Miss Mrs: ")
    return title
    
     
def message (title , fname , lname):
    newmessage ="Welcome {0} {1} {2}".format(title , fname , lname)
    return newmessage

    

fname = name()
lname = last_name()
title = title_name()
newmessage = message (title , fname , lname)
newmessage = newmessage.title()
print(newmessage)
