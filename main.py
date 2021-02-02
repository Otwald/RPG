import click
import os
from test import main
from ini_db import body_gen as Bg, monster_gen as Mg


@click.command()
@click.option(
    '--init',
    help='creates local Memory',
    is_flag=True
)
@click.option(
    '--delete', '-del',
    help='deletes local Memory',
    is_flag=True
)
def cli(init: bool = False, delete: bool = False):
    if init:
        body = Bg.BodyGen()
        body.checkDB()
        mon = Mg.MonsterGen()
        mon.checkDB()
    if delete:
        os.remove('memory.db')
    if not delete and not init:
        main()


# 12312312321
if __name__ == '__main__':
    cli()
