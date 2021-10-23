from modules import calculator_logo

# Operations
def add(n1, n2):
    return n1 + n2
def subtract(n1, n2):
    return n1 - n2
def multiply(n1, n2):
    return n1 * n2
def divide(n1, n2):
    return n1 / n2        

operations = {
    "+" : add,
    "-" : subtract,
    "*" : multiply,
    "/" : divide,
}
# test
# print(operations["+"](1,2))
def calculator():
    print(calculator_logo)
    num1 = float(input("First Number: "))
    oper = input(f"Pick an Operator from {[key for key in operations]}")
    num2 = float(input("Second Number: "))
    result = operations[oper](num1,num2)
    print(f"{num1} {oper} {num2} = {operations[oper](num1,num2)}")

    goon = bool("y" == input("Want to continue calculating?"))
    if not goon:
            if bool("y" == input("Want to start fresh? ")):
                calculator()
    while goon:
        oper = input(f"Pick another Operator from {[key for key in operations]}")
        num3 = float(input("Another Number: "))
        print(f"{result} {oper} {num3} = {operations[oper](result,num3)}")
        result = operations[oper](result,num3)
        goon = bool("y" == input("Want to continue calculating? "))
        if not goon:
            if bool("y" == input("Want to start fresh? ")):
                calculator()
        else:
            pass

calculator()