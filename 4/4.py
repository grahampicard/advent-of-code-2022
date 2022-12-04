def check_subsets(text: str) -> int:
    buf1, buf2 = text.split(",")
    left1, left2 = buf1.split("-")
    right1, right2 = buf2.split("-")
    left1, left2, right1, right2 = [int(x) for x in (left1, left2, right1, right2)]
    left_items = set([x for x in range(left1, left2 + 1)])
    right_items = set([x for x in range(right1, right2 + 1)])
    if left_items.issubset(right_items) or right_items.issubset(left_items):
        return 1
    return 0


def check_any_overlap(text: str) -> int:
    buf1, buf2 = text.split(",")
    left1, left2 = buf1.split("-")
    right1, right2 = buf2.split("-")
    left1, left2, right1, right2 = [int(x) for x in (left1, left2, right1, right2)]
    left_items = set([x for x in range(left1, left2 + 1)])
    right_items = set([x for x in range(right1, right2 + 1)])
    if left_items.intersection(right_items) or right_items.intersection(left_items):
        return 1
    return 0


def part_1(filename: str) -> int:
    with open(filename, "r") as f:
        data = f.read()
    pairs = 0
    for pair in data.split("\n"):
        pairs += check_subsets(pair)
    return pairs


def part_2(filename: str) -> int:
    with open(filename, "r") as f:
        data = f.read()
    pairs = 0
    for pair in data.split("\n"):
        pairs += check_any_overlap(pair)
    return pairs


def main():
    assert part_1("4_test.txt") == 2
    print(part_1("4_input.txt"))

    assert part_2("4_test.txt") == 4
    print(part_2("4_input.txt"))


main()
