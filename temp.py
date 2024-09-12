def celsius_to_f(celsius):
    return (celsius * 1.8) + 32

def f_to_celsius(f):
    return (f - 32) * 5/9

def celsius_to_k(celsius):
    return celsius + 273.15

def k_to_celsius(kelvin):
    return kelvin - 273.15

def f_to_r(f):
    return f + 459.67

def r_to_f(r):
    return r - 459.67

def temperature_conversion():
    print("Temperature Conversion Program")
    print("Choose an option:")
    print("1. Celsius to Fahrenheit")
    print("2. Fahrenheit to Celsius")
    print("3. Celsius to Kelvin")
    print("4. Kelvin to Celsius")
    print("5. Fahrenheit to Rankine")
    print("6. Rankine to Fahrenheit")
    
    choice = input("Enter your choice (1-6): ")
    
    conversion_functions = {
        "1": (celsius_to_f, "°C", "°F"),
        "2": (f_to_celsius, "°F", "°C"),
        "3": (celsius_to_k, "°C", "K"),
        "4": (k_to_celsius, "K", "°C"),
        "5": (f_to_r, "°F", "°R"),
        "6": (r_to_f, "°R", "°F")
    }
    
    if choice in conversion_functions:
        convert_function, from_unit, to_unit = conversion_functions[choice]
        temperature = float(input(f"Enter temperature in {from_unit}: "))
        result = convert_function(temperature)
        print(f"{temperature}{from_unit} = {result:.2f}{to_unit}")
    else:
        print("Invalid choice.")

temperature_conversion()