import click


FILE = "d5/d5_input.txt"


def _get_file():
    with open(FILE, 'r') as fh:
        contents = fh.readlines()
    return contents


def _read_initial_config(raw_list):
    rows = []

    ind_base = 0

    while ind_base < len(raw_list[0]):
        sublist_ind = ind_base + 1
        row = []
        for sublist in reversed(raw_list[:-1]):
            if sublist[sublist_ind] != ' ':
                row.append(sublist[sublist_ind])
        rows.append(row)
        ind_base += 4

    return rows


def execute_instruction(stack_state, instruction):
    split_inst = instruction.split()

    to_move = int(split_inst[1])
    move_from = int(split_inst[3]) - 1
    move_to = int(split_inst[5]) - 1

    for item in range(to_move):
        if len(stack_state[move_from]) > 0:
            stack_state[move_to].append(stack_state[move_from][-1])
            stack_state[move_from] = stack_state[move_from][:-1]

    return stack_state


def execute_instruction_alt(stack_state, instruction):
    split_inst = instruction.split()

    to_move = int(split_inst[1])
    move_from = int(split_inst[3]) - 1
    move_to = int(split_inst[5]) - 1

    last_ind = len(stack_state[move_from]) - to_move
    stack_state[move_to] += stack_state[move_from][last_ind:]
    stack_state[move_from] = stack_state[move_from][:last_ind]

    return stack_state


@click.command("d5p1")
@click.pass_context
def p1(ctx):
    contents = _get_file()

    ind = 0

    while contents[ind] != '\n':
        ind += 1

    init_config_raw = contents[:ind]
    stacks_state = _read_initial_config(init_config_raw)

    instructions = contents[ind+1:]

    for instruction in instructions:
        stacks_state = execute_instruction(stacks_state, instruction)

    print(''.join([x[-1] if len(x) > 0 else '.' for x in stacks_state]))


@click.command("d5p2")
@click.pass_context
def p2(ctx):
    contents = _get_file()

    ind = 0

    while contents[ind] != '\n':
        ind += 1

    init_config_raw = contents[:ind]
    stacks_state = _read_initial_config(init_config_raw)

    instructions = contents[ind+1:]

    for instruction in instructions:
        stacks_state = execute_instruction_alt(stacks_state, instruction)

    print(''.join([x[-1] if len(x) > 0 else '.' for x in stacks_state]))