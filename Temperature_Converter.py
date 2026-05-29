# Temperature Converter Program

print("Temperature Converter")
print("1. Celsius to Fahrenheit")
print("2. Celsius to Kelvin")
print("3. Fahrenheit to Celsius")
print("4. Fahrenheit to Kelvin")
print("5. Kelvin to Celsius")
print("6. Kelvin to Fahrenheit")

choice = int(input("Enter your choice (1-6): "))

temp = float(input("Enter the temperature value: "))

if choice == 1:
    result = (temp * 9/5) + 32
    print("Temperature in Fahrenheit:", result)

elif choice == 2:
    result = temp + 273.15
    print("Temperature in Kelvin:", result)

elif choice == 3:
    result = (temp - 32) * 5/9
    print("Temperature in Celsius:", result)

elif choice == 4:
    result = (temp - 32) * 5/9 + 273.15
    print("Temperature in Kelvin:", result)

elif choice == 5:
    result = temp - 273.15
    print("Temperature in Celsius:", result)

elif choice == 6:
    result = (temp - 273.15) * 9/5 + 32
    print("Temperature in Fahrenheit:", result)

else:
    print("Invalid choice!")
