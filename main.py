import art
print(art.logo)


def add(n1,n2):
    return n1+n2
def subtract(n1,n2):
    return n1-n2
def multiply(n1,n2):
    return n1*n2
def divide(n1,n2):
    return n1/n2

operations= {    
    "+": "add",
    "-": "subtract",
    "*": "multiply",
    "/": "divide",
}

num1 = int(input("What's the first number?: \n"))
num2 = int(input("What's the second number?: \n"))
for symbol in operations:
    print(symbol)
operation_symbol = input("Pick an operation from above: \n")
results_list = []

calculation_function = operation_symbol[operation_symbol]
answer = calculation_function(num1,num2)


print(f"{num1} {operation_symbol} {num2} = {results_list}")


# continuation = input("Type 'y' to continue calculating with {}, or 'n' to start a new calculation:\n")