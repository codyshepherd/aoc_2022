import click


FILE = "d3/d3_input.txt"


def _get_file():
    with open(FILE, 'r') as fh:
        contents = fh.readlines()
    return contents


def _convert_letter(letter):
    if letter.islower():
        return ord(letter) - 96
    else:
        return ord(letter) - 38


@click.command("d3p1")
@click.pass_context
def p1(ctx):
    contents = _get_file()

    total = 0

    for item in contents:
        item = item.strip()
        half_len = len(item) // 2
        p1 = item[:half_len]
        p2 = item[half_len:]

        common = None

        for letter in p1:
            if letter in p2:
                common = letter
                break

        total += _convert_letter(common)

    print(total)


@click.command("d3p2")
@click.pass_context
def p2(ctx):
    contents = _get_file()
    len_contents = len(contents)

    total = 0
    ind = 0

    while ind < len_contents:
        item0 = contents[ind]
        item1 = contents[ind+1]
        item2 = contents[ind+2]

        common = None

        for letter in item0:
            if letter in item1 and letter in item2:
                common = letter
                break

        total += _convert_letter(common)
        ind += 3

    print(total)