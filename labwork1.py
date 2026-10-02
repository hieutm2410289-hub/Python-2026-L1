while True:
    print("\n===== LAB SESSION 1 =====")
    print("1. Circle area")
    print("2. Celsius to Fahrenheit")
    print("3. Prime number")
    print("4. Perfect number")
    print("5. Favorite color")
    print("6. Range sequences")
    print("7. Remove dollar sign")
    print("8. Extract even numbers")
    print("9. Factorial")
    print("10. Divisors")
    print("11. Distance between two points")
    print("12. Pattern")
    print("0. Exit")

    choice = input("Choose (0-12): ")

    if choice == "0":
        break

    elif choice == "1":
        r = float(input("Enter circle radius? "))
        print("Circle area =", 3.14 * r * r)

    elif choice == "2":
        c = float(input("Enter the temperature in Celsius? "))
        print(c, "(C) =", c * 9 / 5 + 32, "(F)")

    elif choice == "3":
        n = int(input("Enter a number? "))
        prime = n >= 2 and all(n % i for i in range(2, int(n**0.5) + 1))
        print(n, "is a prime number" if prime else "is a NOT prime number")

    elif choice == "4":
        n = int(input("Enter a number? "))
        s = sum(i for i in range(1, n) if n % i == 0)
        print(n, "is a perfect number" if s == n else "is a NOT perfect number")

    elif choice == "5":
        colors = ["Blue", "Yellow", "Black", "Red", "White"]
        color = input("What is your favorite color? ")
        if color in colors:
            print("Your color is at index", colors.index(color), "in my list")
        else:
            print("Sorry, I could not find your color")

    elif choice == "6":
        print("range1:", list(range(7)))
        print("range2:", list(range(1, 11, 3)))
        print("range3:", list(range(5, 0, -1)))
        print("range4:", list(range(6, -3, -2)))

    elif choice == "7":
        s = input("Enter a string: ")
        print(s.replace("$", ""))

    elif choice == "8":
        l = list(map(int, input("Enter integers: ").split()))
        print([x for x in l if x % 2 == 0])

    elif choice == "9":
        n = int(input("Enter a number: "))
        f = 1
        for i in range(1, n + 1):
            f *= i
        print("Factorial =", f)

    elif choice == "10":
        n = int(input("Enter a number: "))
        print([i for i in range(1, n + 1) if n % i == 0])

    elif choice == "11":
        x1, y1 = map(float, input("Enter x1 y1: ").split())
        x2, y2 = map(float, input("Enter x2 y2: ").split())
        print("Distance =", ((x2-x1)**2 + (y2-y1)**2) ** 0.5)

    elif choice == "12":
        m = int(input("Enter m: "))
        n = int(input("Enter n: "))
        for i in range(m):
            print("* " * n)

    else:
        print("Invalid choice!")