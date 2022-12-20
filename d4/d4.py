import click


FILE = "d4/d4_input.txt"


def _get_file():
    with open(FILE, 'r') as fh:
        contents = fh.readlines()
    return contents


def _convert_range_to_set(range):
    pair = range.split('-')
    ind = int(pair[0])
    end = int(pair[1])

    items = []

    while ind <= end:
        items.append(str(ind))
        ind += 1

    return set(items)


@click.command("d4p1")
@click.pass_context
def p1(ctx):
    contents = _get_file()

    num_fully_contained = 0

    for item in contents:
        item = item.strip()
        item_t = tuple(item.split(','))

        g1 = _convert_range_to_set(item_t[0])
        g2 = _convert_range_to_set(item_t[1])

        if g1 <= g2 or g2 <= g1:
            num_fully_contained += 1

    print(num_fully_contained)


@click.command("d4p2")
@click.pass_context
def p2(ctx):
    contents = _get_file()

    num_partially_contained = 0

    for item in contents:
        item = item.strip()
        item_t = tuple(item.split(','))

        g1 = _convert_range_to_set(item_t[0])
        g2 = _convert_range_to_set(item_t[1])

        if not g1.isdisjoint(g2):
            num_partially_contained += 1

    print(num_partially_contained)