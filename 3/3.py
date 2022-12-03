import string


def find_shared_items(text: str) -> list[str]:
    h1, h2 = text[: len(text) // 2], text[len(text) // 2 :]
    return [letter for letter in set(h1) if letter in h2]


def priority_sum(text: str) -> int:
    lookup = {a: i + 1 for i, a in enumerate(string.ascii_letters)}
    priority = 0
    for line in text.split("\n"):
        matches = find_shared_items(line)
        for m in matches:
            priority += lookup[m]
    return priority


def part_1():
    # tests
    with open("3_test.txt", "r") as f:
        data = f.read()
    assert priority_sum(data) == 157

    # input
    with open("3_input.txt", "r") as f:
        data = f.read()
    print(priority_sum(data))


def find_second_shared(rucksack: list[str]) -> list[str]:
    any_match = {}
    for sack in rucksack:
        for letter in set(sack):
            if letter not in any_match:
                any_match[letter] = 1
            else:
                any_match[letter] += 1
    full_match = []
    for k, v in any_match.items():
        if v >= len(rucksack):
            full_match.append(k)
    return full_match


def second_priority(text: str) -> int:
    all_lines = text.split("\n")
    lookup = {a: i + 1 for i, a in enumerate(string.ascii_letters)}
    buffer = []
    matches = []
    for line in all_lines:
        buffer.append(line)
        if len(buffer) == 3:
            matches.extend(find_second_shared(buffer))
            buffer = []
    priority = 0
    for m in matches:
        priority += lookup[m]
    return priority


def part_2():
    # tests
    with open("3_test.txt", "r") as f:
        data = f.read()
    assert second_priority(data) == 70

    # input
    with open("3_input.txt", "r") as f:
        data = f.read()
    print(second_priority(data))


part_1()
part_2()
