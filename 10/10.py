def part_1(text: str, cycles: list) -> int:
    instructions = text.split("\n")
    cycle = 0
    buffer = [0]
    X = 1
    results = []
    while buffer:
        X += buffer.pop(0)
        cycle += 1
        if instructions:
            current_instruction = instructions.pop(0)
            if current_instruction == "noop":
                buffer.append(0)
            else:
                new_val = int(current_instruction.split(" ")[1])
                buffer.append(0)
                buffer.append(new_val)
        if cycle in cycles:
            cycles.remove(cycle)
            results.append(X * cycle)
    return sum(results)


def part_2(text: str, cycles: list) -> int:
    instructions = text.split("\n")
    cycle = 0
    buffer = [0]
    X = 1
    results = []
    while buffer:
        X += buffer.pop(0)
        cycle += 1
        if instructions:
            current_instruction = instructions.pop(0)
            if current_instruction == "noop":
                buffer.append(0)
            else:
                new_val = int(current_instruction.split(" ")[1])
                buffer.append(0)
                buffer.append(new_val)
        if cycle in cycles:
            cycles.remove(cycle)
            results.append(X * cycle)

    return sum(results)


def main():
    with open("10_test.txt", "r") as f:
        data = f.read()
        assert part_1(data, [3, 5]) == 23

    with open("10_test2.txt", "r") as f:
        data = f.read()
        assert part_1(data, [20, 60, 100, 140, 180, 220]) == 13140

    with open("10_input.txt", "r") as f:
        data = f.read()
        print(part_1(data, [20, 60, 100, 140, 180, 220]))


main()
