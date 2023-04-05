import copy

visited = []
states = [0, 0, 0, 0]


# finds the position of empty box
def find_pos(s):
    for i in range(len(s)):
        for j in range(len(s[0])):
            if s[i][j] == 0:
                return [i, j]
    return [-1, -1]


# heuristic
# finds distance between two states
def find_distance(cur, goal):
    count = 0
    for i in range(len(cur)):
        for j in range(len(cur[0])):
            if cur[i][j] != goal[i][j]:
                count = count + 1
    return count


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


def search(s, g):
    global visited
    global states
    q = []
    while 1:
        print(find_distance(s,g))
        if s == g:
            print("yes")
            return
        visited.append(s)

        states[0] = up(s)
        states[1] = down(s)
        states[2] = left(s)
        states[3] = right(s)
        for i in range(len(states)):
            print(find_distance(states[i],g))
            if states[i] not in visited and find_distance(states[i],g) < find_distance(s,g):
                q.append(states[i])

        if len(q) == 0:
            print("Can't reach goal")
            return

        min = q[0];
        for i in range(len(q)):
            if q[i] not in visited and find_distance[min,g] > find_distance[q[i],g]:
                min = q[i]

        s = min

    print("Not possible to reach goal")


def main():
    global visited
    start = [[2, 8, 3], [1, 5, 4], [7, 6, 0]]
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    search(start, goal)
    print(len(visited))


if __name__ == "__main__":
    main()
