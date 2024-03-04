print("This is a calculator that executes basic arithmetic, only!")
           
def sum_arithmetic(a , b):
    sum_ = a + b 
    return sum_
    
def subtraction_arithmetic(a, b):
    minus = a - b
    return minus 
def multiple_arithmetic(a, b):
    multiplication = a * b
    return multiplication

def division_arithmetic(a, b):
    division = a / b
    if b == 0:
        return "Error! You can't divide by zero"
    else: 
        return division


def choice():  
    TUPLE_LIST = ("1","2","3","4")
    print("Please select an arithmetic to conduct:") 
    print("1) Addition")
    print("2) Subtraction")
    print("3) Multiplication")
    print("4) Division")
    
    user_input = input("Enter your choice: ")
    
    if user_input in TUPLE_LIST:
        num_a = input("Enter a: ")
        num_b = input("Enter b: ")
        
        if num_a.replace('.', '', 1).isdigit() and num_b.replace('.', '', 1).isdigit():
            num_a = float(num_a)
            num_b = float(num_b)
            if user_input == "1":
                print(num_a, " + ", num_b, " = ", sum_arithmetic(num_a, num_b))
                
            elif user_input == "2":
                print(num_a, " - ", num_b, " = ", subtraction_arithmetic(num_a, num_b))
                
            elif user_input == "3":
                print(num_a, " * ", num_b, " = ", multiple_arithmetic(num_a, num_b))
            
            elif user_input == "4":
                print(num_a, " / ", num_b, " = ", division_arithmetic(num_a, num_b))
    else:
        print("Invalid input")
            
choice()

  