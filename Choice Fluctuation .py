#started 5/10/19 after I woke up with a concept for a simulation based on constantly changing probability
#spent two hours to get it working somewhat, will work on removing values that "die' (become zero) and will
#work on collecting stats and producing a distribution based off this simulation
#5/11/19, In one hour this morning I've made a lot of progress. The game now removes values that are zero
#until there is only one value left, and I've got all the mechanisms for gathering statistics completed.
CFdata = open("CFdata.txt", "w")
import random
import itertools as it
trials = int(input("Enter the number of trials desired: "))
num = int(input("Enter the number of sects desired: "))
#valid nums if the total is 100: {2,4,5,10,20,25,50}
iterList = []        
p = 0
iter = 0
Valid = True
for t in range(0, trials):
    game = []
    for s in range(0, num):
        game.append(int(100/num)) #to add terms at the start of the game        
    while Valid:
        game = list(filter((0).__ne__, game)) #from stackexchange
        if len(game) == 1:
            Valid = False
            break
        x = random.randint(1,101) #on 5/14 I realised I had the range (0,100) when it should have been (1,101)... not major but facepalm lol.
        for n in range(0, len(game)):
            p += game[n]
            if x <= p:
                iter += 1
                game[n] += len(game) - 1
                for o in it.chain(range(0, n), range(n + 1, len(game))):
                    game[o] -= 1
                game[n] = str(game[n]) #This prints every round of the game with the chosen option highlighted
                print("The random number generated was:", x, "The set is:", game, "This is the " + str(iter) + "th round")#x = the random number, p = the sum of all the terms needed to be >= than x
                game[n] = int(game[n])
                p = 0
                break
        
    iterList.append(iter)
    CFdata.write(str(iter)+"\n")
    Valid = True
    iter = 0
    """print(t) #prints iter-count"""
    
"""iterList.sort()
print("The mean value is:", sum(iterList)/len(iterList))
print("The median value is:", int((iterList[int(trials/2)] + iterList[int(trials/2 - 1)]) / 2))
print("The minimum value is:", min(iterList),"\nThe maximum value is:", max(iterList))"""
CFdata.close()