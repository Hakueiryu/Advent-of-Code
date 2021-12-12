from collections import defaultdict

state_space = defaultdict(list)
paths = 0

def graph_search_dfs(state, seen):
    global paths

    if state == 'end':
        paths += 1
        return
    if state.islower() and state in seen:
        return
    seen = seen | {state}
    for next_state in state_space[state]:
        graph_search_dfs(next_state, seen)

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    for x in file:
        a,b = x.split('-')
        state_space[a].append(b)
        state_space[b].append(a)

    graph_search_dfs('start', set())

    print(f'Part 1: {paths}')


