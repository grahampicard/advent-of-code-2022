class Tree:
    def __init__(self, name, parent=None) -> None:
        self.directories = {}
        self.files = {}
        self.size = 0
        self.name = name
        self.parent = parent
    
    def add_directory(self, directory_name) -> None:
        self.directories[directory_name] = Tree(directory_name, self)

    def add_files(self, file_name, size) -> None:
        self.files[file_name] = size

    def _calculate_sizes(self) -> int:
        total = 0
        for directory in self.directories.values():
            total += directory._calculate_sizes()
        for val in self.files.values():
            total += val
        self.size = total
        return total

    def _find_sizes(self, sizes=[]) -> list:
        for directory in self.directories.values():
            directory._find_sizes(sizes)
        sizes.append(self.size)
        return sizes

    def get_sizes(self):
        sizes = []
        self._calculate_sizes()
        return self._find_sizes(sizes)

def read_terminal_output(text: str) -> Tree:
    tree = Tree("")
    all_lines = text.split("\n")
    current_directory = tree
    while all_lines:
        line = all_lines.pop(0)
        if line == "$ cd ..":
            current_directory = current_directory.parent

        elif "$ cd" in line:
            name = line.split(" ")[-1]
            current_directory.add_directory(name)
            current_directory = current_directory.directories[name]
            
        elif line == "$ ls":
            buffer = []
            while all_lines[0][0] != "$":
                output = all_lines.pop(0)
                buffer.append(output)
                if not all_lines:
                    break
            for item in buffer:
                val1, val2 = item.split(" ")
                if val1 == "dir":
                    current_directory.add_directory(val2)
                elif val1.isnumeric():
                    current_directory.add_files(val2, int(val1))
        
    return tree

def part_1(text: str) -> int:
    tree = read_terminal_output(text)
    values = tree.get_sizes()
    return sum([x for x in values if x <= 100000])

def part_2(text: str) -> int:
    tree = read_terminal_output(text)
    values = tree.get_sizes()
    total_size = max(values)
    free_space = 70000000 - total_size
    return min([x for x in values if free_space + x >= 30000000])

def part_1_tests():
    with open("7_test.txt", "r") as f:
        data = f.read()
        t = part_1(data)
        assert part_1(data) == 95437
        assert part_2(data) == 24933642

    with open("7_input.txt", "r") as f:
        data = f.read()
        print(part_1(data))
        print(part_2(data))

part_1_tests()