import typer

import src.main as main

from os import listdir
from subprocess import call


def pcb2printer(boardfile: str, wirefile: str, outfile: str = "out", height: float = 0.5, stl: bool = False, dpi: int = 200, endsize: float = -1):
    model = main.main(boardfile, wirefile, height, dpi, endsize)
    if stl:
        print(f" DOES NOT WORK. Generating stl file {outfile}.stl from boardfile {boardfile} and wirefile {wirefile}.")
        main.saveStl(model, outfile)

    else:
        print(f"Generating scad file {outfile}.scad from boardfile {boardfile} and wirefile {wirefile}.")
        main.saveStl(model,  outfile)


if __name__ == "__main__":
    typer.run(pcb2printer)