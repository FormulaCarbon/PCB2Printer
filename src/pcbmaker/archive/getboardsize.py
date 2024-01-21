from PIL import Image

filePath = "board.png"
board = Image.open(filePath)
 
width = board.width
length = board.height

print("The height of the image is: ", length) 
print("The width of the image is: ", width) 