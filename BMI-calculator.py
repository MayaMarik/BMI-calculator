#inserting weight in kilograms:
print ("insert your weight in kilograms:")
weight = float(input())

#inserting height in meters:
print ("Insert your height in meters:")
height = float(input())

#formula for BMI
x = weight/(height**2)

#the weight categories
if x < 18.5:
    print("You are underweight.")
elif x>=18.5 and x<25:
    print("You are normal.")
elif x >= 25 and x < 30:
    print("You are overweight.")
elif x >= 30:
    print("You are obese.")