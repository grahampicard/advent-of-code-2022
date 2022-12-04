def score_round(text: str) -> int:
    legend = {
        "A": "Rock",
        "B": "Paper",
        "C": "Scissors",
        "X": "Rock",
        "Y": "Paper",
        "Z": "Scissors",
    }
    wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    choices = {"Rock": 1, "Paper": 2, "Scissors": 3}
    opp, me = text.split(" ")
    conv_opp, conv_me = legend[opp], legend[me]
    score = choices[conv_me]
    if wins[conv_opp] == conv_me:
        pass
    elif conv_opp == conv_me:
        score += 3
    elif wins[conv_me] == conv_opp:
        score += 6
    return score


def score_game(text: str) -> int:
    score = 0
    for cur_round in text.split("\n"):
        score += score_round(cur_round)
    return score


def part_1():
    # tests
    with open("2_test.txt", "r") as f:
        data = f.read()
    assert score_game(data) == 15

    # input
    with open("2_input.txt", "r") as f:
        data = f.read()
    print(score_game(data))


def score_round_part2(text: str) -> int:
    legend = {"A": "Rock", "B": "Paper", "C": "Scissors"}
    wins = {"Rock": "Scissors", "Paper": "Rock", "Scissors": "Paper"}
    losses = {v: k for k, v in wins.items()}
    choices = {"Rock": 1, "Paper": 2, "Scissors": 3}
    opp, me = text.split(" ")
    conv_opp = legend[opp]
    score = 0
    if me == "X":
        score += choices[wins[conv_opp]]
    elif me == "Y":
        score += choices[conv_opp] + 3
    elif me == "Z":
        score += choices[losses[conv_opp]] + 6
    return score


def score_second_game(text: str) -> int:
    score = 0
    for cur_round in text.split("\n"):
        score += score_round_part2(cur_round)
    return score


def part_2():
    # tests
    with open("2_test.txt", "r") as f:
        data = f.read()
    assert score_second_game(data) == 12

    # input
    with open("2_input.txt", "r") as f:
        data = f.read()
    print(score_second_game(data))


part_1()
part_2()
