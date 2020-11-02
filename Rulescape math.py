#originally made in mid-February.
#revisited and vastly improved on April 7th and 8th, 2019.
import random

trials = 1
rolls = 10000
accuracy = 3

trialCount = 0

addPropList = []
replacePropList = []
removePropList = []
overflowPropList = []
addPropAvg = 0 
replacePropAvg = 0
removePropAvg = 0
overflowPropAvg = 0

for num in range (0, trials):
    num_of_cards = 2
    number_rolled = 0
    worCount = 0
    addCount = 0
    replaceCount = 0
    removeCount = 0
    overflowCount = 0
    num_of_iter = 0
    cardList = []
    while num_of_iter < rolls:
        number_rolled = random.randint(1,6)
        if num_of_cards == 0:
            if number_rolled <= 3:
                num_of_cards += 1
                addCount += 1
            elif 4 <= number_rolled <= 5:
                num_of_cards += 0
                replaceCount += 1
            else:
                num_of_cards += 0
                removeCount += 1
                worCount += 1
                
        elif num_of_cards == 1:
            if number_rolled <= 3:
                addCount += 1
                num_of_cards += 1
            elif 4 <= number_rolled <= 5:
                replaceCount += 1
            else:
                removeCount += 1
                num_of_cards -= 1
                
        elif 2 <= num_of_cards <= 5:
            if number_rolled <= 3:
                addCount += 1
                num_of_cards += 1
            elif 4 <= number_rolled <= 5:
                replaceCount += 1
            else:
                removeCount += 1
                num_of_cards -= 1
                
        else:
            if number_rolled <= 3:
                overflowCount += 1
                num_of_cards = 2
            elif 4 <= number_rolled <= 5:
                replaceCount += 1          
            else:
                removeCount += 1
                num_of_cards -= 1 
                
        num_of_iter += 1
        cardList.append(num_of_cards)
        
    DigitCount = [cardList.count(num) for num in range(0,7)]
    for num in range(0,7):
        print("The number of times there are " + str(num) + " cards is:", DigitCount[num], "p =", round(DigitCount[num]/rolls, accuracy))

    addProp = round(addCount/rolls, accuracy)
    replaceProp = round(replaceCount/rolls, accuracy)
    removeProp = round(removeCount/rolls, accuracy)
    overflowProp = round(overflowCount/rolls, accuracy)
    add_and_overflowProp = round((addCount + overflowCount)/rolls, accuracy)
    add_and_overflowError = round(((((rolls / 2) - (addCount + overflowCount)) / rolls) * 100), accuracy)
    replaceError = round(((((rolls / 3) - replaceCount)/ rolls) * 100), accuracy)
    removeError = round(((((rolls / 6) - removeCount)/ rolls) * 100), accuracy)

    print("The total number of Warrants of Removal is:", worCount)
    print("The total number of cards added is:", addCount, "p =", addProp)
    print("The total number of cards replaced is:", replaceCount, "p =", replaceProp)
    print("The total number of cards removed is:", removeCount, "p =", removeProp)
    print("The total number of card overflows is:", overflowCount, "p =", overflowProp)
    print("The proportion of 1s, 2s, and 3s rolled is:", add_and_overflowProp, "The error is:", str(add_and_overflowError) + "%")
    print("The proportion of 4s and 5s rolled is:", replaceProp, "The error is:", str(replaceError) + "%")
    print("The proportion of 6s rolled is:", removeProp, "The error is:", str(removeError) + "%")
    
    addPropList.append(addProp)
    overflowPropList.append(overflowProp)
    
    trialCount += 1
    print("TRIAL COUNT:", trialCount)
    print("")

for value in addPropList:
    addPropAvg += value
for value in overflowPropList:
    overflowPropAvg += value
    
print("The estimated true proportion of addProp is:", addPropAvg / trials)
print("The estimated true proportion of overflowProp is:", overflowPropAvg / trials)

