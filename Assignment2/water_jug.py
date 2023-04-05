import copy

FIRST_CAP = 4
SECOND_CAP = 3

q = []
visited = []
states = [0, 0, 0, 0, 0, 0]


def emp_first_jug(s):
    temp = copy.deepcopy(s)
    temp[0] = 0
    return temp


def emp_second_jug(s):
    temp = copy.deepcopy(s)
    temp[1] = 0
    return temp


def fill_first_jug(s):
    temp = copy.deepcopy(s)
    temp[0] = FIRST_CAP
    return temp


def fill_second_jug(s):
    temp = copy.deepcopy(s)
    temp[1] = SECOND_CAP
    return temp


def first_to_second(s):
    temp = copy.deepcopy(s)
    if temp[0] == 0 or temp[1] == SECOND_CAP:
        return temp
    elif s[0] + s[1] <= SECOND_CAP:
        temp[0] = 0
        temp[1] = s[0] + s[1]
    else:
        temp[0] = s[0] - (SECOND_CAP - s[1])
        temp[1] = SECOND_CAP
    return temp


def second_to_first(s):
    temp = copy.deepcopy(s)
    if temp[1] == 0 or temp[0] == FIRST_CAP:
        return temp
    elif s[0] + s[1] <= FIRST_CAP:
        temp[1] = 0
        temp[0] = s[0] + s[1]
    else:
        temp[1] = s[1] - (FIRST_CAP - s[0])
        temp[0] = FIRST_CAP
    return temp


def search(start, goal):
    global q
    global visited
    global states
    while 1:
        if start == goal:
            print("Reached goal")
            return
        if start not in visited:
            visited.append(start)
        states[0] = emp_first_jug(start)
        states[1] = emp_second_jug(start)
        states[2] = fill_first_jug(start)
        states[3] = fill_second_jug(start)
        states[4] = first_to_second(start)
        states[5] = second_to_first(start)

        for i in range(len(states)):
            if states[i] not in visited and states[i] not in q:
                visited.append(states[i])
                q.append(states[i])

        if len(q) == 0:
            print("can't reach goal")
            return
        # start = q.pop(0) # bfs
        start = q.pop()  # dfs


def main():
    start = [0, 0]
    goal = [2, 0]
    search(start, goal)
    print(len(visited))


if __name__ == "__main__":
    main()
