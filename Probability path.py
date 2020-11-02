#Idea taken from work I did while at Dillons May 2019. Found it recorded in my small pink journal. Never got to a satisfactory answer at the time.
#started April 6th, 2020 at 11:23pm

#We are seaching for the expected number of iterations it takes for the value 1 to be selected. I have done this before with my program Lifespan of
#an Everchanging RNG but that was to see broad trends. I want to be more precise and learn the cause of the patterns.
from statistics import mean

trials = 10
g = 3 #number of groups
h = 1 - 1/g
G = list(range(2, g + 1))
GList = []
CountList = []
PropList = []

for a in range(trials):
    for x in G:
        for y in range(1, x + 1):
            GList.append(y)

    #print(GList)
    for b in range(g):
        CountList.append(GList.count(b + 1))
    #print(CountList, "Total =", len(GList))
    for c in range(len(CountList)):
        PropList.append(CountList[c] / len(GList))
    #print(PropList)
    print("Iteration " + str(a+1) + ": P(1) =", round(PropList[0], 3), ", P(1') =", 1 - round(PropList[0], 3), "Expected Duration:",  round(mean(GList), 3))
    GList = [x for x in GList if x != 1] #trimming the 1s
    G = GList[:]
    #print(GList)
    del GList[:]
    del CountList[:]
    del PropList[:]
