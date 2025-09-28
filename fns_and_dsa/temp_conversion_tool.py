FAHRENHEIT_TO_CELSIUS_FACTOR = 5/9
CELSIUS_TO_FAHRENHEIT_FACTOR = 9/5

def convert_to_fahrenheit(celcius):
        return (temp * CELSIUS_TO_FAHRENHEIT_FACTOR) + 32

def convert_to_celsius(fahrenheit):
        return (temp - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

temp = float(input("Enter the temperature to convert: "))

confirm = input("Is this temperature in Celsius or Fahrenheit? (C/F):").upper()

if confirm == "C":
    print("f{temp}°C is {convert_to_fahrenheit(temp)}")
elif confirm == "F":  
    print("f{temp}°F is {convert_to_celsius(temp)}")        
else:
    print("Invalid temperature. Please enter a numeric value.")

