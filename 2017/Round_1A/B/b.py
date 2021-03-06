def set_limits(r):
    pos = 0
    for i in r:
        r[pos] = (float(i) * 0.9, float(i) * 1.1)
        pos += 1

def check_pak(pak, lim):
    for p in range(len(pak)):
        for l in range(len(lim)):
            if float(pak[p]) < float(lim[l]):
                return False

    return True

def possibles_packages(element, lim):
    rtn = []

    start = element // lim

    # Superior from start
    cont = True
    actual = start
    while cont:
        ratio = element / (actual * lim)
        if ratio >= 0.9 and ratio <= 1.1:
            rtn.append(actual)
            actual += 1
        else:
            cont = False
    
    # Inferior from start
    cont = True
    actual = start - 1
    while cont and actual != 0:
        ratio = element / (actual * lim)
        if ratio >= 0.9 and ratio <= 1.1:
            rtn.append(actual)
            actual -= 1
        else:
            cont = False

    
    return rtn



def min_max_servings(pak, lim):
    
    possibles = possibles_packages(pak, lim)
    if len(possibles) == 0:
        return 0

    #print('pak: {}, lim: {}, possibles: {}'.format(str(pak), str(lim), str(sorted(possibles))))

    return (sorted(possibles))

def hasElement(listOfList, element):
    listIdx = -1
    for _list in listOfList:
        listIdx += 1
        if element in _list[1]:
            return (True, listIdx)
    
    return (False,0)

def answer():

    num_ingred, num_pack = map(int, input().split())
    receita = list(map(int, input().split()))

    mat = []
    # Get materials
    for ingr in range(num_ingred):
        mat.append(list(map(int, input().split())))

    # Calculate how much servings each item for each
    # ingredient can do and store in an dictionary,
    # where key is the ingr number.
    candidates = {}
    for ingr in range(num_ingred):
        candidates[ingr] = []
        for pak in range(num_pack):
            candidates[ingr].append((True, min_max_servings(mat[ingr][pak], receita[ingr])))
        
        candidates[ingr] = sorted(candidates[ingr])
    print('candidates: {}'.format(str(candidates)))

    # Count number of right packages where can be formed
    #starting with the min number to max.
    answ = 0
    for pack in range(num_pack):
        servings = candidates[0][pack][1]

        print('servings: ' + str(servings))
        
        for serv in servings:
            has = True
            foundIdx = [0]
            for ingr in range(1, num_ingred):
                el = hasElement(candidates[ingr], serv)
                print('el: ' + str(serv))
                if el[0]:
                    foundIdx.append(el[1])
                else:
                    has = False
                    break

        
            # if found serv in every ingredient
            if has:
                answ += 1
                print('passei')
            else:
                print('else passei')





        


 
    return str(1)

times = int(input())

for t in range(1,times+1):
    print('Case #{}: {}'.format(str(t), answer()))