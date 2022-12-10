def check_neighbors(i: int, j: int, grid: list) -> int:
    is_visible = 1
    for left in range(j):
        if grid[i][left] >= grid[i][j]:
            is_visible = 0
    if is_visible == 1:
        return is_visible
    else:
        is_visible = 1
    for right in range(j + 1, len(grid[0])):
        if grid[i][right] >= grid[i][j]:
            is_visible = 0
    if is_visible == 1:
        return is_visible
    else:
        is_visible = 1
    for top in range(i):
        if grid[top][j] >= grid[i][j]:
            is_visible = 0
    if is_visible == 1:
        return is_visible
    else:
        is_visible = 1
    for bottom in range(i + 1, len(grid)):
        if grid[bottom][j] >= grid[i][j]:
            is_visible = 0

    return is_visible


def part_1(data: str) -> int:
    grid = [[int(y) for y in list(x)] for x in data.split("\n")]
    total = 0
    grid_length = len(grid[0])
    for i in range(len(grid)):
        for j in range(grid_length):
            val = 0
            if (i == 0) or (j == 0):
                val = 1
            elif (i == (grid_length - 1)) or (j == (grid_length - 1)):
                val = 1
            else:
                val = check_neighbors(i, j, grid)
            total += val

    return total


def scenic_score(i: int, j: int, grid: list) -> int:
    left_visible = 0
    current_tree = grid[i][j]
    for left in range(j):
        idx = j - left - 1
        left_visible += 1
        if grid[i][idx] >= current_tree:
            break

    right_visible = 0
    for right in range(j + 1, len(grid[0])):
        right_visible += 1
        if grid[i][right] >= current_tree:
            break

    top_visible = 0
    for top in range(i):
        idx = i - top - 1
        top_visible += 1
        if grid[idx][j] >= current_tree:
            break

    bottom_visible = 0
    for bottom in range(i + 1, len(grid)):
        bottom_visible += 1
        if grid[bottom][j] >= current_tree:
            break

    return left_visible * right_visible * top_visible * bottom_visible


def part_2(data: str) -> int:
    grid = [[int(y) for y in list(x)] for x in data.split("\n")]
    top_view = 0
    grid_length = len(grid[0])
    for i in range(len(grid)):
        for j in range(grid_length):
            cur_view = scenic_score(i, j, grid)
            # print(i, j, cur_view)
            if cur_view > top_view:
                top_view = cur_view
    return top_view


def main():
    with open("8_test.txt", "r") as f:
        data = f.read()
        # Part 1
        assert part_1(data) == 21

        # Part 2
        assert part_2(data) == 8

    with open("8_input.txt", "r") as f:
        data = f.read()
        # Part 1
        print(part_1(data))

        # Part 2
        print(part_2(data))


main()
