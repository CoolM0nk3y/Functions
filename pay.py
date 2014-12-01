

#calculate basic pay
def calculate_basic_pay(hours,rate):
    total = hours * rate
    return total

#calculate the over time pay

def calculate_overtime(hours,rate):
    over_time = hours - 40
    basic_pay = 40 * rate
    overtime_pay = over_time * rate * 1.5
    total = overtime_pay + basic_pay
    return total
# the statment 
def calculate_total_pay(hours,rate):
    if hours <= 40:
        total = calculate_basic_pay(hours,rate)
    else:
        total = calculate_overtime(hours,rate)
    return total

# Get the data from the user
def get_data():
    hours = int(input("Please enter the numbers of hours you do: "))
    rate = int(input("Please enter the rate of pay you have: "))
    return hours , rate 

#calculate basic pay
def calculate_pay():
    hours,rate = get_data ()
    total_pay = calculate_total_pay (hours,rate)
    dis_pay (total_pay)
    
#display the total
def dis_pay (total_pay):
    print(total_pay) 
    


#main program
calculate_pay()




