
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

num1 = int(input("What's the first number?: "))
num2 = int(input("What's the second number?: "))

for key in oper:
    print(key)

def userChoice(self):
    decide_oper = input("Pick an operation from the line above: ")
    
    if decide_oper in oper:
        self.oper[decide_oper]