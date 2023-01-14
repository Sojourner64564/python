def print_average(arr):
    sum = 0
    for i in range(len(arr)):
        sum+=arr[i]
    average=sum/len(arr)
    print(average)
