sum = 0
A = 0
B = 0
list = list(range(1, 10000000))
choice = input("Would you like to add a certain number of terms (Enter: A) or\nWould you like to add until a certain sum (Enter: B): ")
    
if choice == 'A':
    term = int(input("How many terms do you want to add?: ")) + 1
    for n in range (1, term):
        sum += (1/n)
    print(sum)

#Due to list range the maximum sum goal is about 16.
elif choice == 'B':
    goal = float(input("What sum do you want to reach?: "))
    for n in list:
        if sum < goal:
            sum += (1/n)
        else:
            print("The number of terms it took was", n, "and the final sum was:", sum)
            break
