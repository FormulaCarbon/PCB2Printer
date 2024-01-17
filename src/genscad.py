from solid2 import *
from PIL import Image

import genboardimage
from getboardsize import length, width

import genwiringimage

wiringImg = Image.open("wiring.png")
alpha = wiringImg.split()[-1]
pix = alpha.load()

wires = cube(0)
for y in range(0, length-1):
    for x in range(0, width-1):
        if pix[x, y] == 0:
            wires += cube(1.01).translate(x, y, 9)

        print(x,y)

wireInverter = cube([width, length, 1]).translate(00,0,9.5)
invWires = wireInverter-wires

height = 10

board = cube([length, width, height]).rotate(0, 0, -90).translate(0, length, 0)

model = board - wires
model.save_as_scad()
print(wires)