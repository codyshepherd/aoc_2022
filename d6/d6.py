import click


FILE = "d6/d6_input.txt"


def _get_file():
    with open(FILE, 'r') as fh:
        contents = fh.readlines()
    return contents


@click.command("d6p1")
@click.pass_context
def p1(ctx):
    contents = _get_file()[0]

    start_ind = 0
    end_ind = 4

    counter = 4

    while end_ind <= len(contents):
        if len(set(contents[start_ind:end_ind])) == 4:
            break
        else:
            start_ind += 1
            end_ind += 1
            counter += 1

    print(counter)


@click.command("d6p2")
@click.pass_context
def p2(ctx):
    contents = _get_file()[0]

    start_ind = 0
    end_ind = 14

    counter = 14

    while end_ind <= len(contents):
        if len(set(contents[start_ind:end_ind])) == 14:
            break
        else:
            start_ind += 1
            end_ind += 1
            counter += 1

    print(counter)
