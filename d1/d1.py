import click


FILE = "d1/p1_input.txt"


def _get_file():
    with open(FILE, 'r') as fh:
        contents = fh.readlines()
    return contents


@click.command("d1p1")
@click.pass_context
def p1(ctx):
    contents = _get_file()

    elves_list = []
    elf = 0
    for raw in contents:
        if raw == '\n':
            elves_list.append(elf)
            elf = 0
        else:
            elf += int(raw)

    elves_list = sorted(elves_list, reverse=True)
    print(elves_list[0])


@click.command("d1p2")
@click.pass_context
def p2(ctx):
    contents = _get_file()

    elves_list = []
    elf = 0
    for raw in contents:
        if raw == '\n':
            elves_list.append(elf)
            elf = 0
        else:
            elf += int(raw)

    elves_list = sorted(elves_list, reverse=True)
    print(sum(elves_list[:3]))