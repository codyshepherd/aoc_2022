import click


FILE = "d7/d7_input.txt"


class Node(object):

    def __init__(self, name, offset, parent):
        self.name = name
        self.offset = offset
        self.parent = parent
        self.pad = ''.join([' ' for i in range(self.offset*2)])

    def list(self):
        pass

    def list_s(self):
        pass


class Directory(Node):

    def __init__(self, name, offset, parent):
        super().__init__(name, offset, parent)
        self.dirs = {}
        self.files = []
        self.size = 0
        self.small = True

    def list(self):
        print(f"{self.pad}{self.size} {self.name}/")
        for k in self.dirs.keys():
            _dir = self.dirs[k]
            if _dir is not None:
                _dir.list()
        for _file in self.files:
            _file.list()

    def list_s(self):
        string = f"{self.pad}{self.size} {self.name}/\n"
        for k in self.dirs.keys():
            _dir = self.dirs[k]
            if _dir is not None:
                subdir_s = _dir.list_s()
                string += f"{subdir_s}"
            for _file in self.files:
                subdir_s = _file.list_s()
                string += f"{subdir_s}\n"
        return string

    def mkdir(self, name):
        self.dirs[name] = Directory(name, self.offset+1, self)

    def touch(self, name, size):
        self.files.append(File(name, self.offset+1, self, size))
        self.size += size
        if self.size >= 100000:
            self.small = False


class File(Node):

    def __init__(self, name, offset, parent, size):
        super().__init__(name, offset, parent)
        self.size = size

    def list(self):
        print(f"{self.pad}{self.size}  {self.name}")

    def list_s(self):
        return f"{self.pad}{self.size}  {self.name}"


def _get_file():
    with open(FILE, 'r') as fh:
        contents = fh.readlines()
    return contents


def execute(root, instructions):
    if len(instructions) < 1:
        return root, []
    pop = instructions[0]
    if pop.startswith("$ cd .."):
        return root, instructions[1:]
    elif pop.startswith("$ cd"):
        parts = pop.split()
        name = parts[2]
        root.dirs[name], new_instructions = execute(root.dirs[name], instructions[1:])
        root.size += root.dirs[name].size
        return execute(root, new_instructions)
    elif pop.startswith("$ ls"):
        return execute(root, instructions[1:])
    elif pop.startswith("dir"):
        parts = pop.split()
        name = parts[1]
        root.mkdir(name)
        return execute(root, instructions[1:])
    else:
        parts = pop.split()
        name = parts[1]
        size = parts[0]
        root.touch(name, int(size))
        return execute(root, instructions[1:])


def traverse(root):

    if len(root.dirs.keys()) < 1:
        return root.size if root.small else 0
    else:
        if root.small:
            size = root.size
        else:
            size = 0
        sum = size
        for child in root.dirs.keys():
            sum += traverse(root.dirs[child])
        return sum


@click.command("d7p1")
@click.pass_context
def p1(ctx):
    contents = _get_file()

    fs, _ = execute(Directory('/', 0, None), contents[1:])
    #fs.list()
    string = fs.list_s()

    sum = 0
    for item in string.strip().split('\n'):
        if '/' in item:
            size = item.strip().split()[0]
            if int(size) <= 100000:
                sum += int(item.split()[0])
    print(sum)