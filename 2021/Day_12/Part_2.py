from collections import defaultdict

state_machine = defaultdict(list)
paths = 0

def graph_search_dfs(state, seen, seen_twice):
    global paths

    if state == 'end':
        paths += 1
        return
    if state == "start" and seen:
        return
    if state.islower() and state in seen:
        if not seen_twice:
            seen_twice = state
        else:
            return
    seen = seen | {state}
    for next_state in state_machine[state]:
        graph_search_dfs(next_state, seen, seen_twice)
    return

out = graph_search_dfs("start", set(), None)

if __name__ == '__main__':
    file = open('input.txt', 'r').read().strip().split('\n')
    for x in file:
        a,b = x.split('-')
        state_machine[a].append(b)
        state_machine[b].append(a)

    graph_search_dfs('start', set(), None)

    print(f'Part 2: {paths}')