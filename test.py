# print("My name is Arm", "18 years old", "I love sleeping", sep = "\n")

# name = input("Please enter your name: ")
# print("Hello, welcome", name)

temp = float(input("Enter your temperature in Celsius: "))
temp_f = temp * 9/5 + 32  # Convert to Fahrenheit
temp_k = temp + 273.15    # Convert to Kelvin
temp_r = (temp + 273.15) * 9/5  # Convert to Rankine

print(f"Your temperature in Fahrenheit is {temp_f}")
print(f"Your temperature in Kelvin is {temp_k}")
print(f"Your temperature in Rankine is {temp_r}")
