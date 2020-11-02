import random
pList = []

for num in range (0,500): #number of samples
    y = 0
    x = 0
    notx = 0
    count = 0
    for num in range (0,10): #number of choices
        a = random.randint(1,2)
        count += 1
        if a == 1:
            y = True
            x += 1
        if a == 2:
            y = False
            notx += 1
            
    #print("Heads:", x)
    #print("Tails:", notx)
    proportion = round(x/count, 3)
    #print("P-hat:", proportion)
    pList.append(proportion)
    
#print("list of P-hat:", pList)
average = 0
for value in pList:
    average += float(value)
print("The average of all P-hats:", average/500)

chanceList = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

DigitCount = [pList.count(num) for num in chanceList]
for num in range(0,11):
    print("The number of 0." + str(num) + "'s is:", DigitCount[num])

