from solid2 import *
from PIL import Image

import src.genBoardRef as genBoardRef
import src.genWiringRef as genWiringRef
import src.helpers as helpers

def main(boardfile, wiringfile, height = 10, dpi = 200, endsize = 0):
    
    genBoardRef.genBoardImage(boardfile, dpi)
    genWiringRef.genWiringImage(wiringfile, dpi)
    
    wiringImg = Image.open("/tmp/__wires.png")
    alpha = wiringImg.split()[-1]
    pix = alpha.load()
    
    width, length = helpers.getBoardSize()

    wires = cube(0)
    for y in range(0, length-1):
        for x in range(0, width-1):
            if pix[x, y] == 0:
                wires += cube(1.01).translate(x, y, 9)

    #wireInverter = cube([width, length, 1]).translate(00,0,9.5)
    #invWires = wireInverter-wires

    board = cube([length, width, height]).rotate(0, 0, -90).translate(0, length, 0)

    model = board - wires

    if endsize == 0:
        return model
    else:
        return model.scale(endsize/length)

def saveScad(model, outfile):
    model.save_as_scad(outfile)

def saveStl(model, outfile):
    model.save_as_stl(outfile)