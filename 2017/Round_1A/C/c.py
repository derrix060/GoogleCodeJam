def answer():
    return str(1)

times = int(input())

for t in range(1,times+1):

    print('Case #{}: {}'.format(str(t), answer()))