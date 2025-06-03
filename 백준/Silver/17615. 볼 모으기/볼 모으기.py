def count_moves(color, balls):
    # 왼쪽으로 모을 때
    left = 0
    while left < len(balls) and balls[left] == color:
        left += 1
    left_count = balls[left:].count(color)

    # 오른쪽으로 모을 때
    right = len(balls) - 1
    while right >= 0 and balls[right] == color:
        right -= 1
    right_count = balls[:right+1].count(color)

    return min(left_count, right_count)

N = int(input())
balls = input().strip()

print(min(count_moves('R', balls), count_moves('B', balls)))