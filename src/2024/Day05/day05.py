def calculate(line_of_rules: list[str], line_of_pages: list[str]):
    def reorder_pages(pages, rules):
        # Use the rules to sort the pages correctly
        dependencies = {page: set() for page in pages}
        for rule in rules:
            l = rule.split("|")
            if int(l[0]) in pages and int(l[1]) in pages:
                dependencies[int(l[1])].add(int(l[0]))
        sorted_pages = sorted(pages, key=lambda x: len(dependencies[x]))
        return sorted_pages

    total_sum = 0
    total_corrected_sum = 0

    for line in line_of_pages:
        pages = list(map(int, line.split(",")))
        check = True

        for r in line_of_rules:
            l = r.split("|")
            if int(l[0]) in pages and int(l[1]) in pages:
                if pages.index(int(l[0])) > pages.index(int(l[1])):
                    check = False
                    break

        if check:
            print(f"Line is correct: {line}")
            middle = len(pages) // 2
            total_sum += pages[middle]
        else:
            print(f"Line is incorrect: {line}")
            corrected_pages = reorder_pages(pages, line_of_rules)
            print(f"Corrected line: {corrected_pages}")
            middle = len(corrected_pages) // 2
            total_corrected_sum += corrected_pages[middle]

    return total_sum, total_corrected_sum


def read_example():
    line_of_rules: list[str] = []
    line_of_pages: list[str] = []
    with open("example.txt", "r") as file:
        for line in file.readlines():
            if "|" in line:
                line_of_rules.append(line.strip())
            if "," in line:
                line_of_pages.append(line.strip())
    return line_of_rules, line_of_pages


def read_input():
    line_of_rules: list[str] = []
    line_of_pages: list[str] = []
    with open("input.txt", "r") as file:
        for line in file.readlines():
            if "|" in line:
                line_of_rules.append(line.strip())
            if "," in line:
                line_of_pages.append(line.strip())
    return line_of_rules, line_of_pages


if __name__ == "__main__":
    print("Day 5")
    print("Part 1")
    line_of_rules, line_of_pages = read_example()
    sum_correct, sum_corrected = calculate(line_of_rules, line_of_pages)
    print(f"Total sum of correct updates: {sum_correct}")
    print(f"Total sum of corrected updates: {sum_corrected}")
    print("Part 2")
    line_of_rules, line_of_pages = read_input()
    sum_correct, sum_corrected = calculate(line_of_rules, line_of_pages)
    print(f"Total sum of correct updates: {sum_correct}")
    print(f"Total sum of corrected updates: {sum_corrected}")
