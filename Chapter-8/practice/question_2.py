def conversion():
    choice = input("Do you want to convert from Celsius to Fahrenheit (C) or Fahrenheit to Celsius (F)? ").strip().upper()

    if choice == 'C':
        celsius = float(input("Enter the temperature in Celsius: "))
        fahrenheit = round((9/5) * celsius + 32,2)

        print(f"{celsius}°C is equal to {fahrenheit}°F.")

    elif choice == 'F':
        fahrenheit = float(input("Enter the temperature in Fahrenheit: "))
        celsius = round((5/9) * (fahrenheit - 32),2)
        print(f"{fahrenheit}°F is equal to {celsius}°C.")

    else:
        print("Invalid choice! Please enter 'C' or 'F'.")

conversion()

