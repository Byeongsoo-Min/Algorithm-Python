p, m = map(int, input().split())
li = []
for i in range(p):
    lev, name = input().split()
    putIn = False
    for idx, l in enumerate(li):
        if len(l) >= m:
            continue
        if abs(int(lev) - l[0][0]) <= 10:
            li[idx].append((int(lev), name))
            putIn = True
            break
    if not putIn:
        li.append([(int(lev), name)])

for l in li:
    if len(l) == m:
        print("Started!")
    else :
        print("Waiting!")
        
    l.sort(key=lambda x:x[1])
    for s in l:
        print(*s)