"""
8th Gulf Programming Contest   
Zayed Univ. 2018 
D. Flu Epidemic
"""
import math


def explore(person, infected, room, infectors, visited):
    col, row, inc = person
    rowInBound = row >= 0 and row < len(room)
    colInBound = col >= 0 and col < len(room)
    if not rowInBound or not colInBound:
        return room
    print(room[col][row], person, math.dist(person[:2], infected[:2]))
    if room[col][row] == "X" or person in visited:
        return room

    # if math.dist(person[:2], infected[:2]) > 0:
    in_range = math.dist(person[:2], infected[:2]) in range(0, 4)  # TODO: replace 3 and try 3.1
    if not in_range:
        return room

    # if room[col][row] == "I":
    print(person)

    room[col][row] = "I"
    infectors.add(person)
    visited.add(person)
    returned = room
    returned = explore((col - 1, row, inc), infected, room, infectors, visited)
    returned = explore((col, row - 1, inc), infected, room, infectors, visited)
    returned = explore((col, row + 1, inc), infected, room, infectors, visited)
    returned = explore((col + 1, row, inc), infected, room, infectors, visited)
    return returned


def count_infected(room, cured_after, inc_period, infect_rad, staying_duration):
    infectors = set()
    visited = set()
    for i, row in enumerate(room):
        for j, person in enumerate(row):
            if person == "I":
                infectors.add((i, j, None))
                room = explore((i, j, None), (i, j, None), room, infectors, visited)

    print(infectors)
    infectors = list(infectors)
    for i in range(len(infectors)):
        col, row, inc = infectors[i]
        if room[col][row] == "P":
            # inc = 20
            room[col][row] = "I"
        # else:
        #     inc += 20
        infectors[i] = (col, row, inc)
    infectors = set(infectors)

    print(infectors)
    for i, row in enumerate(room):
        for j, person in enumerate(row):
            if person == "I":
                infectors.add((i, j, None))
                room = explore((i, j, None), (i, j, None), room, infectors, visited)
    for row in room:
            print(row)
    return infectors

def main():
    while True:
        w, h = map(int, input().strip().split())
        if w == 0 and h == 0:
            return

        cured_after, inc_period, infect_rad, staying_duration = map(int, input().strip().split())
        room = []
        for _ in range(h):
            room.append(list(input().strip()))
        for row in room:
            print(row)

        print(count_infected(room, cured_after, inc_period, infect_rad, staying_duration))

if __name__ == "__main__":
    main()