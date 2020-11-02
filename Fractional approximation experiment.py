#initialize values
n = 1
sum = 0
count = 1
termList = []
Margin_of_Error = 0.000001
#F = float(input("Enter decimal value here: "))
F = 0.0054

while sum < F:
    count += 1
    n *= 0.5
    sum += n
    if sum > F:
        sum -= n
        continue
    termList.append(count)
    print("The term added is", n, "or 1/(2^" + str(count - 1) + ") and the cumulative sum is:", str(sum))
    if (F - sum) < Margin_of_Error:
        sum = F

