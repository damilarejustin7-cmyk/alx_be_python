from temp_conversion_tool import FAHRENHEIT_TO_CELSIUS_FACTOR, CELSIUS_TO_FAHRENHEIT_FACTOR

def convert_to_celsius(fahrenheit):
    # Convert Fahrenheit to Celsius using the global factor
    return (float(fahrenheit) - 32) * FAHRENHEIT_TO_CELSIUS_FACTOR

def convert_to_fahrenheit(celsius):
    # Convert Celsius to Fahrenheit using the global factor
    return float(celsius) * CELSIUS_TO_FAHRENHEIT_FACTOR + 32

if __name__ == "__main__":
    # Ask user for input
    temp_str = input("Enter the temperature to convert: ").strip()
    unit = input("Is this temperature in Celsius or Fahrenheit? (C/F): ").strip().upper()

    try:
        # Convert input to float (supports decimals)
        temperature = float(temp_str)
    except ValueError:
        # Raise the exact error from the prompt
        print("Invalid temperature. Please enter a numeric value.")
    else:
        # Perform conversion based on the unit
        if unit == "C":
            result = convert_to_fahrenheit(temperature)
            print(f"{temperature:.2f}°C is {result:.2f}°F")
        elif unit == "F":
            result = convert_to_celsius(temperature)
            print(f"{temperature:.2f}°F is {result:.2f}°C")
        else:
            print("Invalid unit. Please enter 'C' or 'F'.")


