
def get_password():
        password = input("please enter a password:")
        return password
def validdate (password):
        valid = False
        length = len(password)
        if 8 <= length <= 20:
                print("password accepted")
                valid = True
        elif length <8:
                print("password too short")

        else :
                print("password too long")
        return valid
def check ():
        valid = False
        while valid ==False:
                password = get_password()
                valid = validdate (password)
check()
                

    
