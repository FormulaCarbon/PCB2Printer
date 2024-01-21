# PCB2Printer
A python program that converts gerber files into an openscad program, to be exported into stl.

note: i made this in like an hour and i never worked with gerber files nor openscad before so the code is bad and it slow.

## how to use
download all files in the pcbmaker folder. To run the program, run the command `py -m pcb2printer PATH_TO_BOARD_FILE PATH_TO_WIRE_FILE`. use `py -m pcb2printer --help` for full information on how to use.

it will throw an error but thats ok. just open `NAME_OF_OUTFILE.stl.scad`. the program may output the file without an extension. if it does, then just add `.scad` to the end.
