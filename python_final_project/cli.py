import fire
from .ascii import convert
from typing import Optional


def cli(image: str, output):
    with open(output, "w") as f:
        f.write(convert(image))

    print(f"Wrote output to {output}")


def main():
    fire.Fire(cli)
