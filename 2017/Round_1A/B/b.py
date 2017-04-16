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


def answer():

    num_ingred, num_pack = map(int, input().split())
    receita = list(map(int, input().split()))

    mat = []
    for ingr in range(num_ingred):
        mat.append(list(map(int, input().split())))


    candidates = {}
    for ingr in range(num_ingred):
        candidates[ingr] = []
        for pak in range(num_pack):
            candidates[ingr].append(min_max_servings(mat[ingr][pak], receita[ingr]))
        
        candidates[ingr] = sorted(candidates[ingr])

    
    print('candidates: {}'.format(str(candidates)))

 
    return str(1)

times = int(input())

for t in range(1,times+1):
    print('Case #{}: {}'.format(str(t), answer()))