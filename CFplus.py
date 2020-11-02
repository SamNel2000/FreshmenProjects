#started 5/14/19 to see if instead of 100 as the probability base a larger or different base would fundamentally transform how this works
#One thing I noticed even with large sizes (10000) is that the game always finishes, I do not know whether I will spend the time to deduce
#a pattern for the mean, median, min/max, or sd, but if I do it will have something to do with probability and series
#after an hour more work on 5/15 I have realized a valuable data type will be the proportional difference of the options and for games
#with size greater than two I will try to create an averaged difference or compounded difference, also I think there would be value in
#trying to scale these differences by the iter count and possibly graph that with R
CFdata = open("CFdata.txt", "w")
import random
import itertools as it
trials = int(input("Enter the number of trials desired: "))
size = int(input("Enter the desired size of the game: "))
num = int(input("Enter the number of sects desired: "))
iterList = []        
p = 0
iter = 0
Valid = True
for t in range(0, trials):
    game = []
    for s in range(0, num):
        game.append(int(size/num)) #to add terms at the start of the game        
    while Valid:
        game = list(filter((0).__ne__, game)) #from stackexchange
        if len(game) == 1:
            Valid = False
            break
        x = random.randint(1, size + 1)
        for n in range(0, len(game)):
            p += game[n]
            if x <= p:
                iter += 1
                game[n] += len(game) - 1
                for o in it.chain(range(0, n), range(n + 1, len(game))):
                    game[o] -= 1
                if iter % 25000 == 0: #selective printing
                    game[n] = str(game[n]) #This prints every round of the game with the chosen option highlighted
                    print(game, iter, str(round(((int(game[0]) - int(game[1]))/size) * 100, 4)) + "%") #only works for 2 options
                    game[n] = int(game[n])
                p = 0
                break
        
    """iterList.append(iter)
    CFdata.write(str(iter)+"\n")"""
    Valid = True
    iter = 0
    """print(t) #prints iter-count"""
"""    
iterList.sort()
print("The mean value is:", sum(iterList)/len(iterList))
print("The median value is:", int((iterList[int(trials/2)] + iterList[int(trials/2 - 1)]) / 2))
print("The minimum value is:", min(iterList),"\nThe maximum value is:", max(iterList))
CFdata.close()"""
