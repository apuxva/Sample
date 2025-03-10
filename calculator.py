def calculator():
    print("Simple Calculator")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")
    print("5. Exit")
    
    while True:
        choice = input("Enter choice (1-5): ")

        if choice == '5':
            print("Exiting...")
            break

        if choice in ['1', '2', '3', '4']:
            num1 = float(input("Enter first number: "))
            num2 = float(input("Enter second number: "))

            if choice == '1':
                print("Result:", num1 + num2)
            elif choice == '2':
                print("Result:", num1 - num2)
            elif choice == '3':
                print("Result:", num1 * num2)
            elif choice == '4':
                if num2 == 0:
                    print("Cannot divide by zero")
                else:
                    print("Result:", num1 / num2)
        else:
            print("Invalid choice")

calculator()
