print(__name__)

def str_to_hex(string): return hex(int(string, 16))

canvas = [
    ['0xff', '0xff', '0xff', '0xff'],
    ['0xff', '0xff', '0xff', '0xff'],
    ['0xff', '0xff', '0xff', '0xff'],
    ['0xff', '0xff', '0xff', '0xff'],
]

while 1:
    for row in canvas:
        input("Row (start): " + f'{row}')
        for pixel in row:
            pixel = '0x' + input("Pixel is currently: "+ f'{pixel}'+"  ")
            if pixel == '0x': pixel = str_to_hex('0xff')
            print(pixel)
        input("Row (end): " + str(row) + "\n\n\n")
    input(canvas)
