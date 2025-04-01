def solution(people, limit):
    people.sort(reverse=True)
    boat_people = set()
    length = len(people)
    latest = length - 1
    for i in range(length):
        if i > latest :
            break
        if (people[i] + people[latest]) <= limit:
            peoples = sorted([i, latest])
            boat_people.add(tuple(peoples))
            latest = latest - 1
        else :
            boat_people.add((i, -1))
    return len(boat_people)