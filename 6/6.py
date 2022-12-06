def detect_marker(signal: str, length) -> int:
    split = list(signal)
    buffer = []
    counter = 0
    while split:
        while len(buffer) < length:
            buffer.append(split.pop(0))
            counter += 1
        if len(buffer) == len(set(buffer)):
            return counter
        else:
            buffer.pop(0)
    raise ValueError


def part_1() -> None:
    tests = (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 7),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 5),
        ("nppdvjthqldpwncqszvftbrmjlhg", 6),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 10),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 11),
    )
    for raw, expected in tests:
        assert detect_marker(raw, 4) == expected
    with open("6_input.txt", "r") as f:
        data = f.read()
        print(detect_marker(data, 4))


def part_2() -> None:
    tests = (
        ("mjqjpqmgbljsphdztnvjfqwrcgsmlb", 19),
        ("bvwbjplbgvbhsrlpgdmjqwftvncz", 23),
        ("nppdvjthqldpwncqszvftbrmjlhg", 23),
        ("nznrnfrfntjfmvfwmzdfjlvtqnbhcprsg", 29),
        ("zcfzfwzzqfrljwzlrfnpqdbhtmscgvjw", 26),
    )
    for raw, expected in tests:
        assert detect_marker(raw, 14) == expected
    with open("6_input.txt", "r") as f:
        data = f.read()
        print(detect_marker(data, 14))


def main():
    part_1()
    part_2()


main()
