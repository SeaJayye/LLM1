# Prompts Used:
"""
1. Write me a python function that converts various units of measurement (miles, inches, pounds, grams, celsius, Fahrenheit)
 to their counterparts (kilometres, centimetres, kilograms, ounces, Fahrenheit, celsius) and returns the converted values.

"""

# ----------------------------------------------------------------------------

# ChatGPT Solution

def convert_units(value, from_unit, to_unit):
    # Conversion dictionaries
    distance_conversion = {
        ("miles", "kilometres"): lambda x: x * 1.60934,
        ("kilometres", "miles"): lambda x: x / 1.60934,
        ("inches", "centimetres"): lambda x: x * 2.54,
        ("centimetres", "inches"): lambda x: x / 2.54
    }
    
    weight_conversion = {
        ("pounds", "kilograms"): lambda x: x * 0.453592,
        ("kilograms", "pounds"): lambda x: x / 0.453592,
        ("grams", "ounces"): lambda x: x * 0.035274,
        ("ounces", "grams"): lambda x: x / 0.035274
    }
    
    temperature_conversion = {
        ("celsius", "Fahrenheit"): lambda x: (x * 9/5) + 32,
        ("Fahrenheit", "celsius"): lambda x: (x - 32) * 5/9
    }
    
    # Check for valid conversion
    if (from_unit, to_unit) in distance_conversion:
        return distance_conversion[(from_unit, to_unit)](value)
    elif (from_unit, to_unit) in weight_conversion:
        return weight_conversion[(from_unit, to_unit)](value)
    elif (from_unit, to_unit) in temperature_conversion:
        return temperature_conversion[(from_unit, to_unit)](value)
    else:
        raise ValueError(f"Invalid conversion from {from_unit} to {to_unit}")

# Test cases
print(convert_units(1, "miles", "kilometres"))  # 1.60934
print(convert_units(1, "inches", "centimetres"))  # 2.54
print(convert_units(1, "pounds", "kilograms"))  # 0.453592
print(convert_units(1, "grams", "ounces"))  # 0.035274
print(convert_units(0, "celsius", "Fahrenheit"))  # 32.0
print(convert_units(32, "Fahrenheit", "celsius"))  # 0.0

# LLM additionally specifies that the units should be validated before passing them into the function for additional robustness.