#!/usr/bin/env python
import click

from d1 import d1
from d2 import d2
from d3 import d3
from d4 import d4
from d5 import d5
from d6 import d6
from d7 import d7
# This is a sample Python script.


# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
@click.group()
@click.pass_context
def main(ctx):
    ctx.ensure_object(dict)


main.add_command(d1.p1)
main.add_command(d1.p2)
main.add_command(d2.p1)
main.add_command(d2.p2)
main.add_command(d3.p1)
main.add_command(d3.p2)
main.add_command(d4.p1)
main.add_command(d4.p2)
main.add_command(d5.p1)
main.add_command(d5.p2)
main.add_command(d6.p1)
main.add_command(d6.p2)
main.add_command(d7.p1)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    main()

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
