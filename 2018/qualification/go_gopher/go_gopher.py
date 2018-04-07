def solve_it():
    a = int(input())
    m = []
    r = 2
    max_r = (a // 3)
    x, y = 1, 1
    while x > 0 and y > 0:
        print('{} 2'.format(r))
        x, y = [int(z) for z in input().split(' ')]
        m.append((x, y))
        if r < max_r and (r-1, 1) in m and (r-1, 2) in m and (r-1, 3) in m:
            r += 1


for _ in range(int(input())):
    solve_it()
