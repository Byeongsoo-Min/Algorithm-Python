import sys
from collections import deque
from collections import Counter

input = sys.stdin.readline

N = int(input())
K = int(input())

board = [[0]*N for _ in range(N)]


for i in range(K):
    x, y = map(int, input().split())
    x -= 1
    y -= 1
    board[x][y] = 1

L = int(input())
direction = []

for i in range(L):
    t, c = input().split()
    t = int(t)
    direction.append((t, c))
    
direction = deque(direction)
snake = deque()
head = 0 # 오른쪽: 0, 위: 1, 왼: 2, 아래: 3
headPoint = (0, 0)
snake.append(headPoint)

dx = [[-1, 1, 0], [0, 0, -1], [1, -1, 0], [0, 0, 1]] # 머리가 오른쪽일때 왼쪽으로 돌리기, 오른쪽으로 돌리기, 직진 순
dy = [[0, 0, 1], [-1, 1, 0], [0, 0, -1], [1, -1, 0]] # 머리가 오른쪽일때 왼쪽으로 돌리기, 오른쪽으로 돌리기, 직진 순
time = 0
crash = False

while direction:
    x, y = direction.popleft()
    crash = False # 자신의 몸에 부딪혔거나 밖으로 나갔거나
    for i in range(time, x): 
        headPoint = (headPoint[0] + dx[head][2], headPoint[1] + dy[head][2]) # 머리 이동
        snake.append(headPoint)
        count = Counter(snake)
        
        if count[headPoint] > 1 or N <= headPoint[0] or headPoint[0] < 0 or N <= headPoint[1] or headPoint[1] < 0 : # 부딪혔으면
            crash = True
            time = i
            # print("crash!")
            break
    
        if board[headPoint[0]][headPoint[1]] == 0: # 사과가 없으면
            snake.popleft() # 팝
        else :
            board[headPoint[0]][headPoint[1]] = 0
        
        
    if crash:
        break
    else :
        time = x
    
    if y == "L": # 왼쪽으로 이동이면
        if head == 3 :
            head = 0
        else :
            head += 1
    else : # 오른쪽으로 이동이면
        if head == 0:
            head = 3
        else :
            head -= 1
    
if crash:
    print(time + 1)
else :
    while not crash:
        headPoint = (headPoint[0] + dx[head][2], headPoint[1] + dy[head][2]) # 머리 이동
        if snake.count(headPoint) > 0 or N <= headPoint[0] or headPoint[0] < 0 or N <= headPoint[1] or headPoint[1] < 0 : # 부딪혔으면
            crash = True
            # print("crash!")
            print(time + 1)
            break
        
        if board[headPoint[0]][headPoint[1]] == 0: # 사과가 없으면
            snake.popleft() # 팝
            
        snake.append(headPoint)
        
        time += 1
        