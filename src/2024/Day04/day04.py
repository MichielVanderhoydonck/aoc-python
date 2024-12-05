def part1(matrix: list[str]) -> int:
    substrings = {"XMAS", "SAMX"}

    def count_substrings(s: str) -> int:
        return sum(s.count(sub) for sub in substrings)

    # Rows
    row_counts = map(count_substrings, matrix)
    # Columns
    cols = len(matrix[0])
    rows = len(matrix)
    col_counts = map(
        lambda col: count_substrings("".join(matrix[row][col] for row in range(rows))),
        range(cols),
    )

    # Count diagonals
    def count_diag(start_row, start_col, step_row, step_col) -> int:
        diag_str = ""
        i, j = start_row, start_col
        while 0 <= i < rows and 0 <= j < cols:
            diag_str += matrix[i][j]
            i += step_row
            j += step_col
        return count_substrings(diag_str)

    # Diagonals
    # Top Left -> Bot Right
    top_left_to_bottom_right = sum(
        map(lambda col: count_diag(0, col, 1, 1), range(cols))
    )
    bottom_left_to_top_right = sum(
        map(lambda row: count_diag(row, 0, 1, 1), range(1, rows))
    )
    # Top Right -> Bot Left
    top_right_to_bottom_left = sum(
        map(lambda col: count_diag(0, col, 1, -1), range(cols - 1, -1, -1))
    )
    bottom_right_to_top_left = sum(
        map(lambda row: count_diag(row, cols - 1, 1, -1), range(1, rows))
    )

    return (
        sum(row_counts)
        + sum(col_counts)
        + top_left_to_bottom_right
        + bottom_left_to_top_right
        + top_right_to_bottom_left
        + bottom_right_to_top_left
    )


def part2(matrix: list[str]) -> int:
    def check_xmas(i: int, j: int) -> bool:
        if matrix[i][j] == "A":
            if i > 0 and i < len(matrix) - 1 and j > 0 and j < len(matrix[0]) - 1:
                top_left_to_bottom_right = (
                    matrix[i - 1][j - 1] == "M"
                    and matrix[i][j] == "A"
                    and matrix[i + 1][j + 1] == "S"
                ) or (
                    matrix[i - 1][j - 1] == "S"
                    and matrix[i][j] == "A"
                    and matrix[i + 1][j + 1] == "M"
                )
                top_right_to_bottom_left = (
                    matrix[i - 1][j + 1] == "M"
                    and matrix[i][j] == "A"
                    and matrix[i + 1][j - 1] == "S"
                ) or (
                    matrix[i - 1][j + 1] == "S"
                    and matrix[i][j] == "A"
                    and matrix[i + 1][j - 1] == "M"
                )

                return top_left_to_bottom_right and top_right_to_bottom_left
        return False

    row_range = range(1, len(matrix) - 1)
    col_range = range(1, len(matrix[0]) - 1)

    return sum(
        map(
            lambda i_j: check_xmas(i_j[0], i_j[1]),
            [(i, j) for i in row_range for j in col_range],
        )
    )


def read_input() -> list[str]:
    with open("input.txt", "r") as file:
        return [line.strip() for line in file.readlines()]


if __name__ == "__main__":
    print("Day 4")
    example: list[str] = [
        "MMMSXXMASM",
        "MSAMXMSMSA",
        "AMXSXMAAMM",
        "MSAMASMSMX",
        "XMASAMXAMM",
        "XXAMMXXAMA",
        "SMSMSASXSS",
        "SAXAMASAAA",
        "MAMMMXMMMM",
        "MXMXAXMASX",
    ]
    print("Part 1:")
    print(f"Found {part1(example)} in the example")
    print(f"Found {part1(read_input())} in the input text")
    print("Part 2:")
    print(f"Found {part2(example)} in the example")
    print(f"Found {part2(read_input())} in the input text")
