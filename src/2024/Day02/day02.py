def read_example(dampened: bool = False) -> int:
    lines = [
        "7 6 4 2 1",
        "1 2 7 8 9",
        "9 7 6 2 1",
        "1 3 2 4 5",
        "8 6 4 4 1",
        "1 3 6 7 9",
    ]
    return sum(calc_safety(list(map(int, line.split())), dampened) for line in lines)


def read_input_file(filename: str = "input.txt", dampened: bool = False) -> int:
    with open(filename, "r") as f:
        return sum(calc_safety(list(map(int, line.split())), dampened) for line in f)


def calc_safety(report: list[int], dampened: bool) -> int:
    deltas = calculate_deltas(report)
    if delta_test(deltas):
        return 1
    if dampened:
        return 1 if any(delta_test(calculate_deltas(report[:i] + report[i + 1 :])) for i in range(len(report))) else 0
        
    return 0


def calculate_deltas(report: list[int]) -> list[int]:
    return [b - a for a, b in zip(report, report[1:])]


def delta_test(deltas: list[int]) -> bool:
    return all(1 <= delta <= 3 for delta in deltas) or all(-3 <= delta <= -1 for delta in deltas)


if __name__ == "__main__":
    print("Day 2")
    print("  Part 1")
    print(f"    Example Safety Score: {read_example()}")
    print(f"    Input File Safety Score: {read_input_file()}")
    print("  Part 2")
    print(f"    Example Dampened Safety Score: {read_example(dampened=True)}")
    print(f"    Input File Dampened Safety Score: {read_input_file(dampened=True)}")
