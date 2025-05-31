#Get the input from the user
length = int(input("Enter the size of the pattern:"))

a = 1
while a <= length:
    a += 1
    
    for i in range(0, length):
        print("*", end="")
    print()
