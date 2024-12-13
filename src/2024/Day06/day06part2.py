def solve(input: list[str]):
    directions = ["^", ">", "v", "<"]
    max_steps = len(input) * len(input[0])

    pos = (-1, -1)
    for line in range(len(input)):
        if "^" in input[line]:
            pos = (input[line].index("^"), line)
            break

    visited = set()  
    direction_index = 0

    def move(pos, direction_index):
        x, y = pos
        new_pos = pos

        if directions[direction_index] == "^":
            new_pos = (x, y - 1)
        elif directions[direction_index] == ">":
            new_pos = (x + 1, y)
        elif directions[direction_index] == "v":
            new_pos = (x, y + 1)
        elif directions[direction_index] == "<":
            new_pos = (x - 1, y)

        if 0 <= new_pos[1] < len(input) and 0 <= new_pos[0] < len(input[0]):
            new_cell = input[new_pos[1]][new_pos[0]]
            if new_cell not in {"#", "O"}:
                return new_pos, direction_index, False 
            else:
                direction_index = (direction_index + 1) % 4
                return pos, direction_index, False  
        else:
            print("Out of grid!")
            return pos, direction_index, True 

    print("Visiting next...")
    steps = 0
    while steps < max_steps:
        state = (pos, direction_index)
        if state in visited:
            print(f"Infinite loop detected with state: {state}")
            return True  
        visited.add(state)

        result = move(pos, direction_index)
        pos, direction_index, out_of_grid = result

        if out_of_grid:
            break  

        steps += 1   
    print("No loop detected.")
    return False  


def read_file(name: str):
    with open(name, "r") as file:
        return [line.strip() for line in file.readlines()]


def add_object_to(grid: list[str]):
    result = []
    for y, line in enumerate(grid):
        for x, char in enumerate(line):
            if char == ".":
                copy = grid[:]
                copy[y] = copy[y][:x] + "O" + copy[y][x + 1:]
                result.append(copy)
    return result


if __name__ == "__main__":
    print("Part 2:")
    loops = 0
    print("example")
    grids = add_object_to(read_file("example.txt"))
    for i, grid in enumerate(grids, 1):
        print(f"Testing grid {i}:")
        if solve(grid):
            loops +=1
        print("---")
    print(f"Found {loops} loops")    
    loops = 0
    print("input")
    grids = add_object_to(read_file("input.txt"))
    for i, grid in enumerate(grids, 1):
        print(f"Testing grid {i}:")
        if solve(grid):
            loops +=1
        print("---")
    print(f"Found {loops} loops")    