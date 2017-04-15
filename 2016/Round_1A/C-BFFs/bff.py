def find_pares(bff):
    rtn = []

    for n in range(1, len(bff) + 1):
        prox = bff[n-1]
        prox_prox = bff[prox-1]
        if prox_prox == n:
            rtn.append((n,prox))
    return rtn

def add_pares(visited, pares):
    if len(pares) == 0:
        return 0
    ret = 0
    for (i,n) in pares:
        if i not in visited and n not in visited:
            ret += 2
    return ret

def longestEnd(bff, i, visited, rtn):
    candidates = []
    

    for n in range(1, len(bff) + 1):
        if bff[n-1] == i and n not in visited:
            candidates.append(n)

    if len(candidates) == 0:
        return 0
    rtn = 1
    maior = []

    for n in candidates:
        newVisited = visited
        newVisited.add(n)
        maior.append(rtn + longestEnd(bff, n, newVisited, rtn))
    
    return max(maior)


def longest(bff, i, pares):
    visited = set()
    actual = i
    nxt = bff[actual-1]

    while(nxt not in visited):
        visited.add(actual)
        if bff[nxt-1] in visited:
            if bff[nxt-1] == i:
                visited.add(nxt)
                break

            if bff[nxt-1] == actual and len(visited) > 1:
                visited.add(nxt)
                add_par = add_pares(visited, pares)

                return len(visited) + longestEnd(bff, nxt, visited, 0) + add_par

        actual = nxt
        nxt = bff[nxt-1]

    return len(visited)


def resp():

    n = int(input())

    bff = []
    bff = [int(s) for s in input().split(' ')]
    longe = []

   
    pares = find_pares(bff)

    for i in range(1, n + 1):
        if (i,bff[i-1]) not in pares:
            #não é par
            tmp = longest(bff,i,pares)
            if tmp == n:
                return n
            else:
                longe.append(tmp)

    if len(longe) == 0:
        #só tem pares
        return n
    else:
        return max(longe)

times = int(input())

for t in range(1, times + 1):
    print('Case #{}: {}'.format(str(t), str(resp())))