def collect_temperature(temperature: str):
    if temperature.startswith("C"):
        clean_temp = temperature.removeprefix("C")
        fahrenheit_temp = (int(clean_temp) * 1.8) + 32
        print(f"{temperature} degrees Celsius is converted to {fahrenheit_temp:.2f} degrees Fahrenheit.")
    elif temperature.startswith("F"):
        clean_temp = temperature.removeprefix("F")
        celsius_temp = (int(clean_temp) - 32) * 5/9
        print(f"{temperature} degrees Fahrenheit is converted to {celsius_temp:.2f} degrees Celsius.")
    else:
      print("Invalid input. Please enter the temperature with correct 'C' of 'F' prefix.")


if __name__ == "__main__":
    collect_temperature(input("Please enter a temperature to convert.\nIt must start with C to convert to Fahrenheit or F to convert to Celsius: "))
