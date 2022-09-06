from art import logo
#ADD
def add(n1, n2):
 return n1 + n2

#SUBTRACT
def subtract(n1, n2):
 return n1 - n2

#MULTIPLY
def multiply(n1, n2):
 return n1 * n2

#DIVIDE
def divide(n1, n2):
 return n1 / n2

oper = {"+": add,
        "-": subtract,
        "*": multiply,
        "/": divide
        }

def calculator():
    print(logo)
    num1 = float(input("What's the first number?: "))
    num2 = float(input("What's the second number?: "))
    
    for key in oper:
        print(key)
        
    decide_oper = input("Pick an operation from the line above: ")
    
    cal_func = oper[decide_oper]
    first_answer = cal_func(num1, num2)
    print(f"{num1} {decide_oper} {num2} = {first_answer}")

    i = 0
    loop = 1

    while i < loop:
        decide_oper = input(f"Type 'y' to continue calculating with {first_answer} or 'n' to start another program:  ")
    
        if decide_oper == "y":
            loop += 1
            decide_oper = input("Pick an operation: ")
            numX = int(input("Enter the next number: "))
        
            cal_func = oper[decide_oper]
            ansX = cal_func(first_answer, numX)
            print(f"{first_answer} {decide_oper} {numX} = {ansX}")
            first_answer = ansX
        
        elif decide_oper == "n":
            calculator()
    
        i += 1
calculator()