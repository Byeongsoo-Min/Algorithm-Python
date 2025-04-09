N, M = map(int, input().split())
r, c, d = map(int, input().split())
rooms = []
for _ in range(N):
    rooms.append(list(map(int, input().split())))
    
ending = False
change = False
cnt = 0
x, y = r, c
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]


def rotate_head():
    global d
    if d == 0:
        d = 3
    elif d == 1:
        d = 0
    elif d == 2:
        d = 1
    else :
        d = 2

def go_straight():
    global x, y
    global change
    
    temp_x = x
    temp_y = y
    if d == 0:
        temp_x += dx[0]
        temp_y += dy[0]
    elif d == 1:
        temp_x += dx[1]
        temp_y += dy[1]
    elif d == 2:
        temp_x += dx[2]
        temp_y += dy[2]
    else :
        temp_x += dx[3]
        temp_y += dy[3]
    
    if 0<= temp_x < N and 0 <= temp_y < M:
        if rooms[temp_x][temp_y] == 0:
            x = temp_x
            y = temp_y
            change = True

def check_empty():
    for i in range(4):
        temp_x = x + dx[i]
        temp_y = y + dy[i]
        if 0<= temp_x < N and 0 <= temp_y < M:
            if rooms[temp_x][temp_y] == 0:
                return True
    return False

def go_back():
    global ending, x, y
    if d == 0:
        temp_x = x + 1
        temp_y = y
    elif d == 1:
        temp_x = x
        temp_y = y - 1
    elif d == 2:
        temp_x = x - 1
        temp_y = y
    else :
        temp_x = x 
        temp_y = y + 1
    if 0<= temp_x < N and 0 <= temp_y < M:
        if rooms[temp_x][temp_y] == 1:
            ending = True
            return
        else :
            x = temp_x
            y = temp_y

while not ending:
    if rooms[x][y] == 0:
        rooms[x][y] = 2
        cnt += 1
    elif check_empty():
        change = False
        while not change :
            rotate_head()
            go_straight()
    else :
        go_back()
            
print(cnt)