def convert_length(value, from_unit, to_unit):
    # Conversion factors to meters
    conversion_factors = {
        'meters': 1,
        'kilometers': 1000,
        'miles': 1609.34,
        'feet': 0.3048,
        'inches': 0.0254,
        'centimeters': 0.01,
        'millimeters': 0.001
    }
    meters = value * conversion_factors[from_unit]
    return meters / conversion_factors[to_unit]

def convert_mass(value, from_unit, to_unit):
    # Conversion factors to kilograms
    conversion_factors = {
        'kilograms': 1,
        'grams': 0.001,
        'pounds': 0.453592,
        'ounces': 0.0283495
    }
    kilograms = value * conversion_factors[from_unit]
    return kilograms / conversion_factors[to_unit]

def convert_temperature(value, from_unit, to_unit):
    if from_unit == 'celsius':
        if to_unit == 'fahrenheit':
            return (value * 9/5) + 32
        elif to_unit == 'kelvin':
            return value + 273.15
        return value
    elif from_unit == 'fahrenheit':
        if to_unit == 'celsius':
            return (value - 32) * 5/9
        elif to_unit == 'kelvin':
            return (value - 32) * 5/9 + 273.15
        return value
    elif from_unit == 'kelvin':
        if to_unit == 'celsius':
            return value - 273.15
        elif to_unit == 'fahrenheit':
            return (value - 273.15) * 9/5 + 32
        return value

def convert_volume(value, from_unit, to_unit):
    # Conversion factors to liters
    conversion_factors = {
        'liters': 1,
        'milliliters': 0.001,
        'gallons': 3.78541,
        'quarts': 0.946353,
        'pints': 0.473176,
        'cups': 0.236588
    }
    liters = value * conversion_factors[from_unit]
    return liters / conversion_factors[to_unit]

def unit_converter():
    print("Choose the type of conversion:")
    print("1. Length")
    print("2. Mass")
    print("3. Temperature")
    print("4. Volume")
    
    choice = input("Enter choice (1/2/3/4): ")
    
    if choice == '1':
        value = float(input("Enter the length value: "))
        from_unit = input("Enter the unit to convert from (meters, kilometers, miles, feet, inches, centimeters, millimeters): ").lower()
        to_unit = input("Enter the unit to convert to (meters, kilometers, miles, feet, inches, centimeters, millimeters): ").lower()
        result = convert_length(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
        
    elif choice == '2':
        value = float(input("Enter the mass value: "))
        from_unit = input("Enter the unit to convert from (kilograms, grams, pounds, ounces): ").lower()
        to_unit = input("Enter the unit to convert to (kilograms, grams, pounds, ounces): ").lower()
        result = convert_mass(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
        
    elif choice == '3':
        value = float(input("Enter the temperature value: "))
        from_unit = input("Enter the unit to convert from (celsius, fahrenheit, kelvin): ").lower()
        to_unit = input("Enter the unit to convert to (celsius, fahrenheit, kelvin): ").lower()
        result = convert_temperature(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
        
    elif choice == '4':
        value = float(input("Enter the volume value: "))
        from_unit = input("Enter the unit to convert from (liters, milliliters, gallons, quarts, pints, cups): ").lower()
        to_unit = input("Enter the unit to convert to (liters, milliliters, gallons, quarts, pints, cups): ").lower()
        result = convert_volume(value, from_unit, to_unit)
        print(f"{value} {from_unit} is equal to {result} {to_unit}.")
        
    else:
        print("Invalid choice!")

# Run the converter
unit_converter()
