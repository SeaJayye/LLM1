
def data_conversion(kilometers, inches, pounds, grams, celsius, farenheit):

    converted_mi = kilometers * 0.621371
    converted_cm = inches * 2.54
    converted_kg = pounds * 0.453592
    converted_oz = grams * 0.035274
    converted_c = (celsius * 9 / 5) + 32
    converted_f = (farenheit - 32) * 5 / 9

    # Return the converted measurements
    return (
        converted_mi,
        converted_cm,
        converted_kg,
        converted_oz,
        converted_c,
        converted_f,
    )


# This is the main part of the program. It will run when the script is executed
if __name__ == "__main__":
    # Declare variables for each measurement
    KILOMETERS = 1.0
    INCHES = 1.0
    POUNDS = 1.0
    GRAMS = 1.0
    CELSIUS = 1.0
    FARENHEIGHT = 1.0

    # Call the data_conversion function with the measurements as arguments
    mi, cm, kg, oz, c, f = data_conversion(
        KILOMETERS, INCHES, POUNDS, GRAMS, CELSIUS, FARENHEIGHT
    )

    # Print out the original and converted measurements
    print(f"converting {KILOMETERS}km to miles...\n{mi:.3f}mi\n")
    print(f"converting {INCHES}in to centimeters...\n{cm:.3f}cm\n")
    print(f"converting {POUNDS}lb to kilograms...\n{kg:.3f}kg\n")
    print(f"converting {GRAMS}g to ounces...\n{oz:.3f}oz\n")
    print(f"converting {CELSIUS}C to Fahrenheit...\n{f:.3f}F\n")
    print(f"converting {FARENHEIGHT}F to Celsius...\n{c:.3f}C\n")