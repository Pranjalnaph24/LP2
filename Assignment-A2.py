import heapq

def get_user_input(prompt):
    print(prompt)
    state = []
    values = set()
    for i in range(3):
        while True:
            row_input = input(f"Row {i + 1} (e.g., 1 2 3): ")
            try:
                row = list(map(int, row_input.strip().split()))
                if len(row) != 3 or not all(0 <= n <= 8 for n in row) or not values.isdisjoint(row):
                    raise ValueError
                values.update(row)
                state.append(row)
                break
            except ValueError:
                print("Invalid input. Please enter 3 unique numbers from 0 to 8.")
    return state

def state_to_tuple(state):
    return tuple(tuple(row) for row in state)

def print_board(state):
    for row in state:
        print(" ".join(str(val) if val != 0 else " " for val in row))
    print()

def manhattan_distance(state, goal_position):
    dist = 0
    for r in range(3):
        for c in range(3):
            val = state[r][c]
            if val != 0:
                goal_r, goal_c = goal_position[val]
                dist += abs(r - goal_r) + abs(c - goal_c)
    return dist

def get_neighbors(state):
    neighbors = []
    r, c = next((i, j) for i in range(3) for j in range(3) if state[i][j] == 0)
    moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for dr, dc in moves:
        nr, nc = r + dr, c + dc
        if 0 <= nr < 3 and 0 <= nc < 3:
            new_state = [row[:] for row in state]
            new_state[r][c], new_state[nr][nc] = new_state[nr][nc], new_state[r][c]
            neighbors.append(new_state)
    return neighbors

def a_star(start_state, goal_state):
    goal_position = {val: (r, c) for r, row in enumerate(goal_state) for c, val in enumerate(row)}
    open_set = [(manhattan_distance(start_state, goal_position), 0, start_state, [])]
    visited = set()

    while open_set:
        f, g, current, path = heapq.heappop(open_set)
        state_id = state_to_tuple(current)

        if state_id in visited:
            continue
        visited.add(state_id)

        print(f"Step {len(path)}: (g={g}, h={f - g}, f={f})")
        print_board(current)

        if current == goal_state:
            print("🎉 Puzzle Solved in", len(path), "steps!")
            return path + [current]

        for neighbor in get_neighbors(current):
            if state_to_tuple(neighbor) not in visited:
                new_g = g + 1
                new_h = manhattan_distance(neighbor, goal_position)
                heapq.heappush(open_set, (new_g + new_h, new_g, neighbor, path + [current]))

    print("No solution found.")
    return None

# Run
if __name__ == "__main__":
    initial_state = get_user_input("Enter the initial state (0 for blank):")
    goal_state = get_user_input("Enter the goal state (0 for blank):")
    a_star(initial_state, goal_state)
