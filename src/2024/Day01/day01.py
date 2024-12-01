def calc_dist(left, right):
    return sum(abs(x - y) for x, y in zip(sorted(left), sorted(right)))


def find_sim(left, right):
    return sum(map(lambda val: val * right.count(val), left))


def read_input_file():
    f = open("input.txt", "r")
    lines = map(str.strip, f)
    fields = [(int(l), int(r)) for l, r in map(str.split, lines)]
    [left, right] = [sorted(list(i)) for i in zip(*fields)]

    return left, right


if __name__ == "__main__":
    print("Day 1")
    left = [3, 4, 2, 1, 3, 3]
    right = [4, 3, 5, 3, 9, 3]
    example_distance = calc_dist(left, right)
    example_similarity = find_sim(left, right)
    print(f"the distance in the example is: {example_distance}")
    print(f"the similarity in the example is: {example_similarity}")
    left, right = read_input_file()
    part1_distance = calc_dist(left, right)
    print(f"the distance in the part1 is: {part1_distance}")
    part2_sim = find_sim(left, right)
    print(f"the similarity in the part2 is: {part2_sim}")
