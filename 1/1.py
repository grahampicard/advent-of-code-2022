from typing import List


def prep_elf(text: str) -> List[int]:
    calories = []
    for line in text.split("\n"):
        calories.append(int(line))
    return calories


def get_top_calories(text: str) -> int:
    raw_elves = text.split("\n\n")
    elf_counts = [prep_elf(elf) for elf in raw_elves]
    max_calories = max([sum(x) for x in elf_counts])
    return max_calories


def get_top_three_calories(text: str) -> int:
    raw_elves = text.split("\n\n")
    elf_counts = [prep_elf(elf) for elf in raw_elves]
    calories = sorted([sum(x) for x in elf_counts], reverse=True)
    return sum(calories[:3])


def part_1_tests():
    with open("1_test.txt", "r") as f:
        data = f.read()
    assert get_top_calories(data) == 24000


def part_1():
    with open("1_input.txt", "r") as f:
        data = f.read()
    print(get_top_calories(data))


def part_2_tests():
    with open("1_test.txt", "r") as f:
        data = f.read()
    assert get_top_three_calories(data) == 45000


def part_2():
    with open("1_input.txt", "r") as f:
        data = f.read()
    print(get_top_three_calories(data))


part_1_tests()
part_1()
part_2_tests()
part_2()
