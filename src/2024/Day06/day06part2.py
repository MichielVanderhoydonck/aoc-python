def solve(input: list[str]):
    directions = ["^", ">", "v", "<"]
    max_steps = len(input) * len(input[0])

    def find_start(grid):
        for line_index, line in enumerate(grid):
            if "^" in line:
                return (line.index("^"), line_index)
        raise ValueError("No starting position (^) found in the grid")

    def move(pos, direction_index, grid):
        x, y = pos
        deltas = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
        direction = directions[direction_index]
        dx, dy = deltas[direction]
        new_pos = (x + dx, y + dy)

        if 0 <= new_pos[1] < len(grid) and 0 <= new_pos[0] < len(grid[0]):
            new_cell = grid[new_pos[1]][new_pos[0]]
            if new_cell not in {"#", "O"}:
                return new_pos, direction_index, False
            else:
                direction_index = (direction_index + 1) % 4
                return pos, direction_index, False
        else:
            print("Out of grid!")
            return pos, direction_index, True

    pos = find_start(input)
    direction_index = 0
    visited = set()
    steps = 0

    while steps < max_steps:
        state = (pos, direction_index)
        if state in visited:
            print(f"Infinite loop detected with state: {state}")
            return True
        visited.add(state)

        pos, direction_index, out_of_grid = move(pos, direction_index, input)
        if out_of_grid:
            break 

        steps += 1

    print("No loop detected.")
    return False 


def read_file(name: str):
    with open(name, "r") as file:
        return [line.strip() for line in file.readlines()]


def add_object_to(grid: list[str]):
    new_grids = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == ".":
                new_grid = [row if row_idx != y else row[:x] + "O" + row[x + 1:] for row_idx, row in enumerate(grid)]
                new_grids.append(new_grid)
    return new_grids


if __name__ == "__main__":
    print("Part 2:")
    loops = 0

    print("Example:")
    example_grids = add_object_to(read_file("example.txt"))
    for i, grid in enumerate(example_grids, 1):
        print(f"Testing grid {i}:")
        if solve(grid):
            loops += 1
        print("---")
    print(f"Found {loops} loops")

    loops = 0
    print("Input:")
    input_grids = add_object_to(read_file("input.txt"))
    for i, grid in enumerate(input_grids, 1):
        print(f"Testing grid {i}:")
        if solve(grid):
            loops += 1
        print("---")
    print(f"Found {loops} loops")
