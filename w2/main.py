# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

# Write your code below this line 👇

BMI = int(weight / (height * height))

print(str(BMI) + "\n" + """Hello the following is on to interpret the results above. \n
if you are below 18.5 you are considered underweight \n
between 18.5 - 24.9 Healthy Weight \n
between 25.0 - 29.9 Overwieght \n
and 30 and above is Obsity \n
This is all based on you being 20 years old or older""")
