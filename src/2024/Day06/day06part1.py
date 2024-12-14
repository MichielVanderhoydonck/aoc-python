def solve(input: list[str]):
    directions = ["^", ">", "v", "<"]

    def find_start(input):
        for line_index, line in enumerate(input):
            if "^" in line:
                start_pos = (line.index("^"), line_index)
                print(f"Found ^ at X: {start_pos[0]} Y: {start_pos[1]}")
                return start_pos
        raise ValueError("No starting position (^) found in input")

    def move(pos, direction_index, visited):
        deltas = {"^": (0, -1), ">": (1, 0), "v": (0, 1), "<": (-1, 0)}
        direction = directions[direction_index]
        new_pos = (pos[0] + deltas[direction][0], pos[1] + deltas[direction][1])

        if 0 <= new_pos[1] < len(input) and 0 <= new_pos[0] < len(input[0]):
            cell = input[new_pos[1]][new_pos[0]]
            print(f"Moving to {cell} at position {new_pos} ({direction})")

            if cell != "#":
                return new_pos, direction_index, visited + [new_pos], False
            else:
                print("Collision! Turning 90 degrees right.")
                return pos, (direction_index + 1) % 4, visited, False
        else:
            print("Out of grid!")
            return pos, direction_index, visited, True

    pos = find_start(input)
    visited = [pos]
    direction_index = 0
    out_grid = False

    while not out_grid:
        pos, direction_index, visited, out_grid = move(pos, direction_index, visited)

    print("Distinct visited positions:")
    print(len(set(visited)))


def read_file(name: str):
    with open(name, "r") as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    print("Day 6")
    print("Part 1")
    solve(read_file("example.txt"))
    solve(read_file("input.txt"))
