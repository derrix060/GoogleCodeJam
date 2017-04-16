
def column(matrix,i):
    return [int(row[i]) for row in matrix]

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



def can_use_package(pak, lim):
    candidates_for_servings_per_item = []


    #for each item in package
    for i in range(len(pak)):
        #get (max,min) servings
        possibles = possibles_packages(pak[i], lim[i])
        if len(possibles) == 0:
            return 0
        candidates_for_servings_per_item.append((pak[i], possibles))
    
    print('candidates_for_servings_per_item for item: {}'.format(str(candidates_for_servings_per_item)))

    

    return 0


def answer():

    num_ingred, num_pack = map(int, input().split())
    receita = list(map(int, input().split()))

    mat = []
    for i in range(num_ingred):
        q = input().split(' ')
        mat.append(q)
    
    pakages = []
    validPackages = 0
    for i in range(num_pack):
        pakages.append(column(mat,i))
        validPackages += can_use_package(pakages[i], receita)


    return str(validPackages)

times = int(input())

for t in range(1,times+1):
    print('Case #{}: {}'.format(str(t), answer()))