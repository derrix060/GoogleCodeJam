
def answer():
    numb = {}
    size = int(input())
    resp = []

    for i in range((2 * size)-1):
        row = input().split(" ")

        for j in range(size):
            n = row[j]
            if n in numb:
                numb[n] += 1
            else:
                numb[n] = 1
        
    keys = numb.keys()
    for j in keys:
        if (numb[j] % 2 != 0):
            resp.append(int(j))
    
    resp.sort()

    respS = ""
    for j in resp:
        respS += (" " + str(j))
    
    return respS





t = int(input())

for i in range(1,t+1):

    print('Case #{}:'.format(str(i)) + answer())