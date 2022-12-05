import string


def init_queues(queue_text: str) -> dict:
    queue_start = {}
    start = queue_text.split("\n")
    all_queues = start.pop()
    for i, _ in enumerate(all_queues.split()):
        queue_start[i] = []
    n_keys = len(queue_start)
    while start:
        line = start.pop()
        count = 0
        while count < n_keys:
            box = line[4 * count + 1]
            if box != " ":
                queue_start[count].append(box)
            count += 1
    return queue_start


def parse_instruction(text: str) -> tuple:
    n, src, dest = [
        int(val) for val in text.split() if set(string.digits).issuperset(val)
    ]
    return n, src - 1, dest - 1


def rearrangement_9000(text: str) -> str:
    raw_start, raw_moves = text.split("\n\n")
    queues = init_queues(raw_start)
    split_moves = raw_moves.split("\n")
    while split_moves:
        instruction = split_moves.pop(0)
        n, src, dest = parse_instruction(instruction)
        for _ in range(n):
            queues[dest].append(queues[src].pop())
    message = ""
    for val in queues.values():
        message += val.pop()
    return message


def rearrangement_9001(text: str) -> str:
    raw_start, raw_moves = text.split("\n\n")
    queues = init_queues(raw_start)
    split_moves = raw_moves.split("\n")
    while split_moves:
        instruction = split_moves.pop(0)
        n, src, dest = parse_instruction(instruction)
        stack = []
        for _ in range(n):
            stack.append(queues[src].pop())
        while stack:
            queues[dest].append(stack.pop())
    message = ""
    for val in queues.values():
        message += val.pop()
    return message


def main() -> None:
    with open("5_test.txt", "r") as f:
        data = f.read()
        assert rearrangement_9000(data) == "CMZ"
    with open("5_input.txt", "r") as f:
        data = f.read()
        print(rearrangement_9000(data))
    with open("5_test.txt", "r") as f:
        data = f.read()
        assert rearrangement_9001(data) == "MCD"
    with open("5_input.txt", "r") as f:
        data = f.read()
        print(rearrangement_9001(data))


main()
