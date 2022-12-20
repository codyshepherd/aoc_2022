import click


FILE = "d2/d2_input.txt"
CHOICE_POINTS = {
    "X": 1,
    "Y": 2,
    "Z": 3,
}

CHOICE_RESULT = {
    "X": {
        "A": 3,
        "B": 0,
        "C": 6,
    },
    "Y": {
        "A": 6,
        "B": 3,
        "C": 0,
    },
    "Z": {
        "A": 0,
        "B": 6,
        "C": 3,
    },
}

CHOICE_POINTS_ALT = {
    "A": 1,
    "B": 2,
    "C": 3,
}

WIN_LOSS_POINTS = {
    "X": 0,
    "Y": 3,
    "Z": 6,
}

HOW_TO_CHOOSE = {
    "A": {  # rock
        "X": "C",  # scissors loses
        "Y": "A",  # rock ties
        "Z": "B",  # paper beats rock
    },
    "B": {  # paper
        "X": "A",  # rock loses
        "Y": "B",  # paper ties
        "Z": "C",  # scissors beats paper
    },
    "C": {  # scissors
        "X": "B",  # paper loses
        "Y": "C",  # scissors ties
        "Z": "A",  # rock beats scissors
    },
}


def _get_file():
    with open(FILE, 'r') as fh:
        contents = fh.readlines()
    return contents


def _round_to_points(round):
    choice = round[1]
    opponent = round[0]

    return CHOICE_POINTS[choice] + CHOICE_RESULT[choice][opponent]


def _round_to_points_alt(round):
    result = round[1]
    opponent = round[0]

    return WIN_LOSS_POINTS[result] + CHOICE_POINTS_ALT[HOW_TO_CHOOSE[opponent][result]]

@click.command("d2p1")
@click.pass_context
def p1(ctx):
    contents = _get_file()
    total = 0

    for round in contents:
        round = round.strip().split(' ')
        total += _round_to_points(round)

    print(total)


@click.command("d2p2")
@click.pass_context
def p2(ctx):
    contents = _get_file()
    total = 0

    for round in contents:
        round = round.strip().split(' ')
        total += _round_to_points_alt(round)

    print(total)