import art



def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations= {    
    "+": add,
    "-": subtract,
    "*": multiply,
    "/": divide,
}
def calculator():
    print(art.logo)
    num1 = float(input("What's the first number?: \n"))
    should_continue = True
    while should_continue == True:
        num2 = float(input("What's the next number?: \n"))
        for symbol in operations:
            print(symbol)
        operation_symbol = input("Pick an operation: \n")
        calculation_function = operations[operation_symbol]
        answer = round(calculation_function(num1,num2),2)
        print(f"{num1} {operation_symbol} {num2} = {answer}")
        continuation = input(f"Type 'y' to continue calculating with {answer}, or 'n' to start a new calculation:\n")
        if continuation == 'y':
            num1 = answer
        elif continuation == 'n':
            should_continue = False
            calculator()

calculator()

