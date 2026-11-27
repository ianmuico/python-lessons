weight, height = float(input("Enter your weight in kilograms: ")), float(input("Enter your height in meters: "))

BMI = weight / height ** 2 #BMI calculation formula weight (kg) / height (m)^2

print(f"Your BMI is {BMI:.2f}")