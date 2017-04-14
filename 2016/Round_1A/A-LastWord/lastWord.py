

def rightWord(w):
   ret = ''
   for c in w:
       ret = max(c + ret, ret + c)
   return ret

t = int(input())

for i in range(1, t+1):
    s = input()
    print('Case #{}: {}'.format(i, rightWord(s)))
