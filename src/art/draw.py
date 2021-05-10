print(__name__)

canvas = [
    ['ff', 'ff', 'ff', 'ff'],
    ['ff', 'ff', 'ff', 'ff'],
    ['ff', 'ff', 'ff', 'ff'],
    ['ff', 'ff', 'ff', 'ff'],
]

while 1:
    for row in canvas:
        input("Row (start): " + str(row))
        for pixel in row:
            pixel = input("Pixel is currently: "+pixel+"  ")
            if not pixel: pixel = 'ff'
            print(pixel)
        input("Row (end): " + str(row) + "\n\n\n")
    input(canvas)
