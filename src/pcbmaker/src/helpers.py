from PIL import Image

def getBoardSize():
    filePath = "/tmp/__board.png"
    board = Image.open(filePath)
    
    width = board.width
    length = board.height

    return width, length

    #print("The height of the image is: ", length) 
    #print("The width of the image is: ", width) 