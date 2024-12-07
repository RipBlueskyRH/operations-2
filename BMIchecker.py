w = float (input("enter your weight in kilograms"))
h = float (input("enter your height in meters"))
BMI=w/(h*h)
if BMI <= 18.4:
    print ("you are underweight")
elif BMI <= 24.9:
    print ("you are healthy")
elif BMI <= 29.9:
    print ("you are overweight")
elif BMI <= 34.9:
    print ("you are severely overweight")
elif BMI <= 39.9:
    print ("you are obese")
else:
    print ("i dont want to say anything 😶")