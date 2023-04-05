import copy

q = []
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
    global q
    global states
    q.append([find_distance(s, g), s])
    while q:
        q.sort()
        temp = q.pop(0)
        node = temp[1]
        if node == g:
            print("yes")
            return
        visited.append(node)

        states[0] = up(node)
        states[1] = down(node)
        states[2] = left(node)
        states[3] = right(node)
        for i in range(len(states)):
            if states[i] not in visited and temp not in q:
                q.append([find_distance(states[i], g), states[i]])

    print("Not possible to reach goal")


def main():
    global visited
    start = [[2, 0, 3], [1, 8, 4], [7, 6, 5]]
    goal = [[1, 2, 3], [8, 0, 4], [7, 6, 5]]
    search(start, goal)
    print(len(visited))


if __name__ == "__main__":
    main()
