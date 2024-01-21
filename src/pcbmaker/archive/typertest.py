import typer


def typertest(boardfile: str, wirefile: str, outfile: str = "out", height: float = 0.5, stl: bool = False, dpi: int = 200, endsize: float = -1):
    if stl:
        print(f"Generating stl file {outfile}.stl from boardfile {boardfile} and wirefile {wirefile}.")
    else:
        print(f"Generating scad file {outfile}.scad from boardfile {boardfile} and wirefile {wirefile}.")


if __name__ == "__main__":
    typer.run(typertest)