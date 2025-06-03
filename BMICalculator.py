print("Welcome to the BMI CALCULATOR!")
height = float(input("What is your height in inches?"))
weight = float(input("What is your weight?"))

bmi = weight/ (height ** 2) * 703

print("Your BMI is: " + str(bmi))