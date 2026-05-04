# Input: getting the weight
heightInches = float(input("Enter your height in inches: "))
print(heightInches)
print(type(heightInches))
weightPounds = float(input("Enter your weight in pounds: "))
print(weightPounds)
print(type(weightPounds))

# Calculating BMI = W / H2 × 703
BMI = weightPounds/(heightInches**2) * 703

# Convert to metric
weightKilograms = weightPounds * 0.453592
print(weightKilograms)
print(type(weightKilograms))
heightMeters = heightInches * 0.0254
print(heightMeters)
print(type(heightMeters))

#Calculate BMI Metric
BMIMetric = weightKilograms / (heightMeters**2)

# Display BMI
print(f"BMI: {BMI:.2f}")
print(f"BMI metric: {BMIMetric:.2f}")