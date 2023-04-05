import copy

q = []
visited = []
states = [0, 0, 0, 0]


def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i, j]
    return [-1, -1]


def up(s):
    temp = copy.deepcopy(s)
    pos = find_pos(temp)
    i = pos[0]
    j = pos[1]
    if i > 0:
        temp[i][j] = temp[i - 1][j]
        temp[i - 1][j] = 0
    return temp


def down(s):
    temp = copy.deepcopy(s)
    pos = find_pos(temp)
    i = pos[0]
    j = pos[1]
    if i >= 0 and i < len(s) - 1:
        temp[i][j] = temp[i + 1][j]
        temp[i + 1][j] = 0
    return temp


def left(s):
    temp = copy.deepcopy(s)
    pos = find_pos(temp)
    i = pos[0]
    j = pos[1]
    if j > 0:
        temp[i][j] = temp[i][j - 1]
        temp[i][j - 1] = 0
    return temp


def right(s):
    temp = copy.deepcopy(s)
    pos = find_pos(temp)
    i = pos[0]
    j = pos[1]
    if j >= 0 and j < len(s[0]) - 1:
        temp[i][j] = temp[i][j + 1]
        temp[i][j + 1] = 0
    return temp


def printState(s):
    for i in range(3):
        for j in range(3):
            print(s[i][j], end=" ")
        print(" ", end=" ")
    print()


def search(s, g):
    global visited
    global q
    global states
    q.append(s)
    while q:
        s = q.pop(0)
        if s == g:
            print("yes")
            return
        visited.append(s)

        states[0] = up(s)
        states[1] = down(s)
        states[2] = left(s)
        states[3] = right(s)
        for i in range(len(states)):
            if states[i] not in visited and states[i] not in q:
                q.append(states[i])

    print("Not possible")


def main():
    global visited
    start = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    search(start, goal)
    print(len(visited))


if __name__ == "__main__":
    main()
