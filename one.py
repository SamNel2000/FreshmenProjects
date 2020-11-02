import random
#import matplotlib.pyplot as plt
pList = []
trials = 50 #number of samples
size = 10 #sample size
count = 0

while count < trials:
    heads = 0
    tails = 0
    count2 = 0
    while count2 < size:
        a = random.randint(1, 2)
        if a == 1:
            heads += 1
        else:
            tails += 1
        count2 += 1

    count += 1

    proportion = round(heads / count2, 5)
    pList.append(proportion)

print("list of P-hat:", pList)
average = 0
for value in pList:
    average += float(value)
print("The average of all P-hats:", average / trials)

chanceList = [0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0]

DigitCount = [pList.count(num) for num in chanceList]
for num in range(0, 11):
    if num == 0:
        print("There was", 0, "head", DigitCount[num], "times.")
    else:
        print("There was", num, "heads", DigitCount[num], "times.")

#plt.hist(pList, bins = 11)
#plt.show()