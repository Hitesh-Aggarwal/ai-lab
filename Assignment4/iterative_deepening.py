import copy


def isEqual(s, g):
    for elem in s:
        if elem not in g:
            return 0
    return 1


def is_in_list(s, list):
    for i in range(len(list)):
        if isEqual(list[i], s):
            return 1
    return 0

def is_in_queue(s,q):
    for i in range(len(q)):
        if isEqual(q[i][0],s[0]):
            return 1
    return 0


def generate_children(start):
    state = start[0]
    children = []
    for i in range(len(state)):
        if len(state[i]) != 0:
            box = state[i].pop()
            for j in range(len(state)):
                if j != i:
                    state[j].append(box)
                    if not is_in_list(state, children):
                        children.append([copy.deepcopy(state), start[1] + 1])
                    state[j].pop()
            state[i].append(box)
    return children


def search_aux(start, goal, limit):
    q = []
    visited = []
    q.append([start, 0])
    while q:
        node = q.pop()
        if isEqual(node[0], goal):
            print("Reached goal")
            return visited
        visited.append(node[0])
        states = generate_children(node)
        for i in range(len(states)):
            if (
                not is_in_list(states[i][0], visited)
                and not is_in_queue(states[i], q)
                and states[i][1] <= limit
            ):
                q.append(states[i])
    return 0


def search(s, g):
    i = 0
    res = 0
    while res == 0:
        i = i + 1
        res = search_aux(s, g, i)
    return res


def main():
    start = [["A"], ["B", "C"], []]
    goal = [[], [], ["A", "B", "C"]]
    visited = search(start, goal)
    print(len(visited))


if __name__ == "__main__":
    main()
