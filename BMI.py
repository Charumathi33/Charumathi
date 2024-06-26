w=float(input("enter a weight in KG:"))
h=float(input("enter a height in CM:"))
BMI=w/h**2
if BMI<18.5:
    print("Underweight")
elif BMI>18.5 and BMI<25:
    print("Normal")
elif BMI>=25 and BMI<30:
    print("Overweight")
else:
    print("Obesity")