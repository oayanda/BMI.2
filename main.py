# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
bmi = weight / height ** 2
bmi_value = round(bmi, 0)
if bmi_value < 18.5:
     print(f"Your BMI is {bmi_value}, you are underweight.")
elif bmi_value < 25:
        print(f"Your BMI is {bmi_value}, you are normal weight.")
elif bmi_value < 30:
        print(f"Your BMI is {bmi_value}, you are slightly overweight.")
elif bmi_value < 35:
        print(f"Your BMI is {bmi_value}, you are obses.")
else:
    print(f"Your BMI is {bmi_value}, you are clinically obese.")

    
# print(bmi_value)
