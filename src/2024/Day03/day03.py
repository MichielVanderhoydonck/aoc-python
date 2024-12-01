import re


# https://regexr.com/ I don't like regex
def parse_part1(input: str) -> int:
    return sum(int(n1) * int(n2) for n1, n2 in re.findall(r"mul\((\d+),(\d+)\)", input))


# I still don't like regex
# The expression tries to match muls it can find so the first two indexes of m represent the numbers to multiply
# The third index can be either do or don't
# The non-capturing group helps grouping with the |, two digits are found OR do or don't is captured in index 3
def parse_part2(input: str) -> int:
    total = 0
    enable = True
    matches = re.findall(r"(?:mul\((\d+),(\d+)\))|(do\(\)|don't\(\))", input)
    for match in matches:
        if match[2] == "" and enable:
            total += int(match[0]) * int(match[1])
        else:
            enable = match[2] == "do()"
    return total


if __name__ == "__main__":
    print("Day 3")
    input = "xmul(2,4)%&mul[3,7]!@^do_not_mul(5,5)+mul(32,64]then(mul(11,8)mul(8,5))"
    print("  Part 1:")
    print(f"  Total found for example input is: { parse_part1(input) }")
    with open("input.txt", "r") as f:
        print(f"  Total found for file input is: { parse_part1(f.read().strip()) }")
    print("  Part 2:")
    print(f"  Total found for example input is: { parse_part2(input) }")
    with open("input.txt", "r") as f:
        print(f"  Total found for file input is: { parse_part2(f.read().strip()) }")
