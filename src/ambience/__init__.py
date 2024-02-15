import os
import click
import random
from InquirerPy import inquirer
from InquirerPy.base.control import Choice

from ._sources import sources, Source

COMMAND = "mpv --no-video '{}'"


def _play_source(source: Source) -> None:
    print(f"playing {source.name} with {source.url}")
    os.system(COMMAND.format(source.url))


def _play_random() -> None:
    random_source = random.choice(sources)
    _play_source(random_source)


@click.option("--random", "-r", is_flag=True, default=False)
@click.command()
def main(random: bool = False):
    if random:
        _play_random()
        exit(0)

    while True:
        choices = (
            ["😵 random"]
            + [Choice(source, source.name) for source in sources]
            + ["❌ quit"]
        )

        answer = inquirer.select(
            message="Select a source",
            choices=choices,
        ).execute()

        if answer == "😵 random":
            _play_random()
        elif answer == "❌ quit":
            exit(0)
        else:
            breakpoint()
            _play_source(Source(**answer))
