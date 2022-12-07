import copy

class Node:
    def __init__(self, name) -> None:
        self.directories = {}
        self.files = {}
        self.size = 0
        self.name = name
    
    def add_directory(self, directory_name) -> None:
        self.directories[directory_name] = Node(directory_name)

    def add_files(self, file_name, size) -> None:
        self.files[file_name] = size

    def calculate_total_size(self) -> int:
        total = 0
        for file_size in self.files.values():
            total += file_size
        for directory in self.directories.values():
            total += directory.calculate_total_size()
        self.size = total
        return total



def read_terminal_output(text: str) -> Node:
    tree = Node("")
    all_lines = text.split("\n")
    for line in all_lines:
        if "$ cd" in line:
            name = line.split(" ")[-1]
            # continue here

def get_sizes(tree: Node, sizes=[]) -> list:
    if tree.directories:
        for directory in tree.directories.values():
            sizes = get_sizes(directory, sizes)
    sizes.append(tree.size)
    return sizes      

def part_1(text: str) -> int:
    tree = read_terminal_output(text)
    all_sizes = [x for x in get_sizes(tree) if x <= 100000]
    return sum(all_sizes)

def part_1_tests():
    with open("7_test.txt", "r") as f:
        data = f.read()
        assert part_1(data) == 95437





a = Node()
a.add_files('b.txt', 14848514)
a.add_files('c.dat', 8504156)
a.add_directory('a')
a.directories['a'].add_directory('b')
a.directories['a'].directories['b'].add_files('d', 34343)
a.directories['a'].add_files('c', 10000000000)
a.calculate_total_size()
