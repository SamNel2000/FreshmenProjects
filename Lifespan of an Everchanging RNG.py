#Thought of this idea at work on 5/14/19, and subsequently wrote it down on a Dillons memo to transcribe later
#after over an hour, I learned some stuff, enjoyed manipulating the varaibles, got bored of trying to print
#histograms in R but it's still an intersting idea having random games/simuations that python does. I like it!
#on May 16th (happy birthday me), I am working on finding the formula to predict the probabilities of each count value
lifespan = open("lifespan.txt", "w") #for R
import random
trials = 100000
iterList = []
"""num = int(input("Set the upper bound as: "))  
   trials = int(input("Enter the number of trials desired: ")"""

for n in range(0, trials):
    num = 2 #default should be 100, if num = 2 then the values produced are the same as Sigma n = 2 of 1/2n
    #mean for 2,3,4: 2,2.5,2.83. Basically, every mean is 1/(num - 1) greater than the previous...
    #again with the convergent series as shown above, there is some underlying pattern relating to it.
    count = 0
    while num!= 1:
        num = random.randint(1, num) #default range of the RNG is (1, num)
        count += 1
        #print("[Count: "+ str(count) + ", Number: " + str(num) + "]") #for troubleshooting though I had none when making this
        
    #lifespan.write(str(count)+"\n") #for R
    iterList.append(count) #python data
    
iterList.sort()
print("The mean value is:", sum(iterList)/len(iterList))
print("The median value is:", int((iterList[int(trials/2)] + iterList[int(trials/2 - 1)]) / 2))
print("The maximum value is:", max(iterList), "\n")

#the code below is taken from my Prog 1 course Mod6Dis1
DigitCount = [iterList.count(v) for v in range(1, max(iterList) + 1)]
for num in range(0, max(iterList)):
    print("The number of " + str(num + 1) + "'s is:", DigitCount[num], "or", DigitCount[num] / trials) #general equation
    
lifespan.close() #for R