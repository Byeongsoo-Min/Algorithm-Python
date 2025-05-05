N = int(input())
out = []
op = []
for _ in range(1, N + 1):
    xLine = list(input().split())
    find = False
    if len(xLine) == 1:
        for xL in xLine:
            temp = list(xL)
            for x in range(len(xL)):
                if xL[x].upper() not in op:
                    op.append(xL[x].upper())
                    temp.insert(x, "[")
                    temp.insert(x + 2, "]")
                    find = True
                    break
            if find:
                out.append(temp)
                break
        if not find:
            out.append(xLine)
    else :
        for i in range(len(xLine)):
            temp = list(xLine[i])
            if temp[0].upper() not in op:
                op.append(temp[0].upper())
                temp.insert(0, "[")
                temp.insert(2, "]")
                find = True
                xLine[i] = temp
                break
        if find:
            temp = []
            for i in range(len(xLine) - 1):
                temp.extend(xLine[i])
                temp.extend(" ")
            temp.extend(xLine[-1])
            out.append(temp)
        else :
            for i in range(len(xLine)):
                temp = list(xLine[i])
                for x in range(len(temp)):
                    if temp[x].upper() not in op:
                        op.append(temp[x].upper())
                        temp.insert(x, "[")
                        temp.insert(x + 2, "]")
                        find = True
                        xLine[i] = temp
                        break
                if find:
                    break
            temp = []
            for i in range(len(xLine) - 1):
                temp.extend(xLine[i])
                temp.extend(" ")
            temp.extend(xLine[-1])
            out.append(temp)
for o in out:
    print(''.join(o))