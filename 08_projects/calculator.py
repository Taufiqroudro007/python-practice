print("===== Simple Calculator =====")

while True:
    print("\nChoose an operation:")
    print("1. Addition (+)")
    print("2. Subtraction (-)")
    print("3. Multiplication (*)")
    print("4. Division (/)")
    print("5. Modulus (%)")
    print("6. Exponent (**)")
    print("7. Floor Division (//)")
    print("8. Exit")

    choice = input("Enter your choice (1-8): ")

    if choice == "8":
        print("\nThank you for using the calculator!")
        break

    if choice not in ["1", "2", "3", "4", "5", "6", "7"]:
        print("Invalid choice! Please try again.")
        continue

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == "1":
        print("Result =", num1 + num2)

    elif choice == "2":
        print("Result =", num1 - num2)

    elif choice == "3":
        print("Result =", num1 * num2)

    elif choice == "4":
        if num2 == 0:
            print("Error! Division by zero is not allowed.")
        else:
            print("Result =", num1 / num2)

    elif choice == "5":
        if num2 == 0:
            print("Error! Modulus by zero is not allowed.")
        else:
            print("Result =", num1 % num2)

    elif choice == "6":
        print("Result =", num1 ** num2)

    elif choice == "7":
        if num2 == 0:
            print("Error! Floor division by zero is not allowed.")
        else:
            print("Result =", num1 // num2)
