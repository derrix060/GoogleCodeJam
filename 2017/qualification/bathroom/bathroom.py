import queue

def updateMaxMin(max, min, bath):
    return 1

def solver (stalls, people):

    max = stalls
    min = stalls

    # full
    if (stalls == people):
        return [0,0]

    # start bath
    bath = queue.PriorityQueue()
    bath.put((-stalls, stalls))

    for i in range(people):
        temp = bath.get()[1]
        max = int(temp / 2)
        if temp % 2 == 0:
            min = int(temp / 2 - 1)
        else:
            max = int(temp / 2)

        bath.put((-max,max))
        bath.put((-min,min))
    
    return [max,min]


times = int(input())
for i in range(1, times + 1):
    stalls, people = (int(j) for j in input().split(' '))

    answer = solver (stalls, people) 
    print("Case #{}: {} {}".format(str(i), str(answer[0]), str(answer[1])))
