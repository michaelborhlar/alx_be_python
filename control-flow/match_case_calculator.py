num1 = int(input("Enter the first number: "))
num2 = int(input("Enter the second number: "))

#mathematical operation to be performed
operation = input("Choose the operation (+, -, *, /): ")


match operation:
    case "+":
        result = num1 + num2
        
    case '-':
        result = num1 - num2
    
    case "*":
        result = num1 * num2
        
    case "/":
        if num2 != 0:
            result = num1/num2
        else:
            result = "Math error!"

print("The result is", result) 
            