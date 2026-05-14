def calculate_bmi(weight_kg, height_m):
    """Calculate the Body Mass Index (BMI) given weight and height. Takes two
    arguments weight in kilograms (kg) and height in meters(m). The function returns
    BMI of the weight and height as a float."""

    return weight_kg / (height_m ** 2)

# Example usage
bmi = calculate_bmi (55, 1.67)
print(f"The BMI is: {bmi:.2f}")

