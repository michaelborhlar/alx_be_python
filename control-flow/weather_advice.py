#Get weather details from the user
weather = str(input("What's the weather like today? (sunny/rainy/cold):"))

#Set the conditions for the weather and the result for each conditions
if weather == "sunny":
    print("Wear a t-shirt and sunglasses.")
elif weather == "rainy":
    print("Don't forget your umbrella and a raincoat.")
elif weather == "cold":
    print("Make sure to wear a warm coat and a scarf.")
else:
    print("Sorry, I don't have recommendations for this weather.")

