tc = int(input())

for t in range(1, tc+1):
    num_ingreds, num_packs = map(int, input().split())
    receita = list(map(int, input().split()))
    compra = []
    for _ in range(num_ingreds):
        compra.append(list(map(int, input().split())))
    #print('compra: ' + str(compra))
    qtde_limite = []
    for ingrediente in range(num_ingreds):
        for pacote in range(num_packs):
            units = compra[ingrediente][pacote]
            rec = receita[ingrediente]
            up = (10 * units) // (9 * rec)
            down = (10 * units + 11 * rec - 1) // (11 * rec)
            if down == 0: down = 1
            if up < down: continue
            qtde_limite.append((down, False, ingrediente, units, pacote))
            qtde_limite.append((up, True, ingrediente, units, pacote))
    qtde_limite.sort()
    print('qtde_limite: ' + str(qtde_limite))
    cnt = 0
    counts = [[] for _ in range(num_ingreds)]
    remv = [0] * num_ingreds
    for (qtde, isUp, ingrediente, units, pacote) in qtde_limite:
        #print(counts, remv)
        if isUp:
            if remv[ingrediente] > 0:
                remv[ingrediente] -= 1
            else:
                counts[ingrediente].remove(units)
        else:
            counts[ingrediente].append(units)
            if all(counts):
                cnt += 1
                for ingr_idx in range(num_ingreds):
                    counts[ingr_idx].remove(min(counts[ingr_idx]))
                    remv[ingr_idx] += 1

    print("Case #%{}: {}".format(str(t), str(cnt)))
