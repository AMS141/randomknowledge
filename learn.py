def calc(num1: int, num2: int) -> int | str:
    output = 0
    match choice:
        case "+":
            output = num1 + num2
        case "-":
            output = num1 - num2
        case "*":
            output = num1 * num2
        case "/":
            if num2 == 0:
                output = "Error: Cannot divide by 0"
            else:
                output = num1 / num2
        case "%":
            output = num1 % num2
        case _:
            output = "Invalid choice"

    return output

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
choice = input("Enter your operand: ")

result = calc(num1, num2)
print("Result: ", result)