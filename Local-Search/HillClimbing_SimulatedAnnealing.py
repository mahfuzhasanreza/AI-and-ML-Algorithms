import random
import math

def read_input():
    with open('input.txt', 'r') as file:
        puzzle = [list(map(int, line.split())) for line in file]
    return puzzle

GOAL_STATE = [
    [0, 1, 2],
    [3, 4, 5],
    [6, 7, 8]
]

def hamming_distance(state):
    count = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0 and state[i][j] != GOAL_STATE[i][j]:
                count += 1
    return count

def manhattan_distance(state):
    total_distance = 0
    for i in range(3):
        for j in range(3):
            if state[i][j] != 0:
                correct_position = divmod(state[i][j], 3)
                total_distance += abs(correct_position[0] - i) + abs(correct_position[1] - j)
    return total_distance

def get_neighbors(state):
    neighbors = []
    x, y = [(i, row.index(0)) for i, row in enumerate(state) if 0 in row][0]

    def swap_and_copy(x1, y1, x2, y2):
        new_state = [row[:] for row in state]
        new_state[x1][y1], new_state[x2][y2] = new_state[x2][y2], new_state[x1][y1]
        return new_state

    if x > 0: neighbors.append(swap_and_copy(x, y, x - 1, y))
    if x < 2: neighbors.append(swap_and_copy(x, y, x + 1, y))
    if y > 0: neighbors.append(swap_and_copy(x, y, x, y - 1))
    if y < 2: neighbors.append(swap_and_copy(x, y, x, y + 1))

    return neighbors

def hill_climbing(start_state, heuristic_fn):
    current_state = start_state
    current_score = heuristic_fn(current_state)
    iterations = 0

    while current_score > 0 and iterations < 1000:
        neighbors = get_neighbors(current_state)
        next_state = min(neighbors, key=heuristic_fn)
        next_score = heuristic_fn(next_state)

        if next_score >= current_score:
            break

        current_state, current_score = next_state, next_score
        iterations += 1

    return current_state, current_score, iterations

def simulated_annealing(start_state, heuristic_fn, T0=500, alpha=0.95):
    current_state = start_state
    current_score = heuristic_fn(current_state)
    T = T0
    iterations = 0

    while current_score > 0 and iterations < 1000:
        neighbors = get_neighbors(current_state)
        next_state = random.choice(neighbors)
        next_score = heuristic_fn(next_state)

        delta = next_score - current_score

        if delta < 0 or random.uniform(0, 1) < math.exp(-delta / T):
            current_state, current_score = next_state, next_score

        iterations += 1
        T = T0 / (1 + alpha * iterations)
        if T <= 0:
            break

    return current_state, current_score, iterations

def print_state(state, h, iterations):
    for row in state:
        print(' '.join(str(x) for x in row))
    print(f"h={h}")
    print(f"{iterations} iterations\n")


if __name__ == "__main__":
    initial_state = read_input()

    hc_hamming_result = hill_climbing(initial_state, hamming_distance)
    hc_manhattan_result = hill_climbing(initial_state, manhattan_distance)

    sa_hamming_result = simulated_annealing(initial_state, hamming_distance)
    sa_manhattan_result = simulated_annealing(initial_state, manhattan_distance)

    print("Hill Climbing with Hamming Distance:")
    print_state(hc_hamming_result[0], hc_hamming_result[1], hc_hamming_result[2])

    print("Hill Climbing with Manhattan Distance:")
    print_state(hc_manhattan_result[0], hc_manhattan_result[1], hc_manhattan_result[2])

    print("Simulated Annealing with Hamming Distance:")
    print_state(sa_hamming_result[0], sa_hamming_result[1], sa_hamming_result[2])

    print("Simulated Annealing with Manhattan Distance:")
    print_state(sa_manhattan_result[0], sa_manhattan_result[1], sa_manhattan_result[2])
