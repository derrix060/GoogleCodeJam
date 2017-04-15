
def column(matrix,i):
    return [row[i] for row in matrix]

def minR(r):
    pos = 0
    for i in r:
        r[pos] = float(i) * 0.9
        pos += 1

def check_pak(pak, lim):
    for p in range(len(pak)):
        for l in range(len(lim)):
            if float(pak[p]) < float(lim[l]):
                return False

    return True

def set_num_servings(pak, lim):
    num_paks = []

    for i in range(len(pak)):
        num_paks.append(float(pak[i]) // float(lim[i]))

    print('min: {}, num_paks: {}'.format(str(min(num_paks)), str(num_paks)))
    return min(num_paks)


def answer():

    n, p = [int (s) for s in input().split(' ')]
    r = input().split(' ')
    minR(r)
    print('n: {}, p: {}, r: {}'.format(str(n), str(p), str(r)))

    mat = []
    for i in range(n):
        q = input().split(' ')
        mat.append(q)
    
    pak = []
    result = 0
    for i in range(p):
        pak.append(column(mat,i))
    
    num_servings = set_num_servings(pak[0], r)

    if num_servings == 0:
        return str(0)


    
    
    print('pakages: ' + str(pak))

    return str(1)

times = int(input())

for t in range(1,times+1):
    print('Case #{}: {}'.format(str(t), answer()))