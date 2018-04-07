def swap(s, i, j):
    lst = list(s)
    lst[i], lst[j] = lst[j], lst[i]
    return ''.join(lst)

def calculate_damage(p):
    strength = 1
    damage = 0
    for command in p:
        if command == 'C':
            strength *= 2
        else:
            damage += strength
    return damage

def solve_it():
    d, p = input().split(' ')
    defese = int(d)
    strength = 1
    charge = []
    damage = 0
    for command in p:
        if command == 'C':
            strength *= 2
        else:
            damage += strength
        charge.append(strength)

    if p.count('S') > defese:
        return 'IMPOSSIBLE'

    swaps = 0
    count = 0
    len_p = len(p)
    pos = len_p - count - 1
    while damage > defese:
        pos = len_p - count - 1
        if p[pos] == 'S' and p[pos - 1] == 'C':
            swaps += 1
            p = swap(p, pos, pos-1)
            charge[pos-1] //= 2
            # Better than use calculate_damage
            damage -= charge[pos-1]
            # damage = calculate_damage(p)

        count += 1
        # Start again
        if count == len_p - 1:
            count = 0
    
    return swaps


t = int(input())

for case in range(1, t+1):
    answer = solve_it()
    print('Case #{}: {}'.format(case, answer))