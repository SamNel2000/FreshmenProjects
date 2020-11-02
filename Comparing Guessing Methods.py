#This was written to prove Bi wrong.
#Her claim (from a previous math teacher) is that when guessing on a multiple choice test it is better to pick one letter
#and guess with that same letter throughout the list, I pointed out that it made no difference but she did not believe me
#this was me proving myself right. The conversation happened Wednesday night May 1st, 2019 and I began writing the code on
#paper at Dillons on May 5th, 2019. I completed this code at 3:19pm on May 7th, 2019.
 
import random
t = int(input("Enter the number of trials you want: "))
n = int(input("Enter the number of questions per test: "))
c = int(input("Enter the number of choices per question: "))
a = int(input("Choose method of guessing:\nEnter [1] for same-choice\nEnter [2] for random guess\n"))
plist = []

for test in range(0,t):
    xlist = []
    tcount = 0  
    for q in range(0,n):
        xlist.append(random.randint(1,c))      
    if a == 1:
        g = random.randint(1,c)
        for q in range(0,n):
            if g == xlist[q]:
                tcount += 1
    elif a == 2:
        for q in range(0,n):
            g = random.randint(1,c)
            if g == xlist[q]:
                tcount += 1
    p = tcount/n
    plist.append(p)

max = max(plist) 
min = min(plist) 
mean = round(sum(plist)/t, 6)
expP = 1/c

print("The mean is", mean,"and the expected value is", expP, "and the minimum is", min, "and the maximum is", max)