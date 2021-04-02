# function calculates amount of dog food to order for next month
def nextMonthDogFood(numSmallDog, numMedDog, numLargeDog, remainFood):
    #Calculates how much dog food is needed
    food_total = (((numSmallDog*10) + (numMedDog*20) + (numLargeDog*30))- remainFood)
    # calculates 20% more food needed and adds that to the dog food total
    _moreFood = 0.2 * food_total
    orderFoodAmt = food_total + _moreFood
    # Output the dog food in lbs to order
    print("Food amount to order next month is:",orderFoodAmt,"bls")
    
nextMonthDogFood(5,3,7,17)
