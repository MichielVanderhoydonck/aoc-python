def solve(input: list[str]):
    pos = (-1, -1)
    visited = []
    directions = ["^", ">", "v", "<"]
    direction_index = 0

    for line in range(len(input)):
        print(line)
        if "^" in input[line]:
            print(f"found ^ at X: {input[line].index('^')} Y: {line}")
            pos = (input[line].index("^"), line)
            break

    visited.append(pos)

    def move():
        nonlocal pos, direction_index
        new_pos = None

        if directions[direction_index] == "^":
            new_pos = (pos[0], pos[1] - 1)  # UP
        elif directions[direction_index] == ">":
            new_pos = (pos[0] + 1, pos[1])  # RIGHT
        elif directions[direction_index] == "v":
            new_pos = (pos[0], pos[1] + 1)  # DOWN
        elif directions[direction_index] == "<":
            new_pos = (pos[0] - 1, pos[1])  # LEFT

        # Check if new_pos is valid
        if new_pos is not None:
            # Check if the new position is within the grid
            if 0 <= new_pos[0] < len(input) and 0 <= new_pos[1] < len(input[0]):
                line = input[new_pos[1]]
                new_cell = line[new_pos[0]]
                print(
                    f"Moving to {new_cell} at position {new_pos} ({directions[direction_index]})"
                )

                if new_cell != "#":
                    visited.append(new_pos)
                    pos = new_pos
                    return False
                else:
                    print("Collision! Turning 90 degrees right.")
                    direction_index = (direction_index + 1) % 4
                    return False
            else:
                print("Out of grid!")
                return True
        else:
            print("No valid direction!")
            return True

    print("Visiting next...")
    out_grid = False
    while not out_grid:
        out_grid = move()

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
