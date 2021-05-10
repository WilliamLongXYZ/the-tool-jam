print(__name__)

hex_bytes = ['0x00']
CEND = '\33[0m'

CBLACK = '\033[30m'
CRED = '\033[91m'
CWHITE = '\033[37m'


def read_byte(byte, canvas, location):
    canvas[location[1]][location[0]] = byte

def print_byte(byte):
    if byte == '0x00':
        print(CBLACK + '0' + CEND, end=' ')
    if byte == '0x80':
        print(CRED + '0' + CEND, end=' ')
    if byte == '0xff':
        print(CWHITE + '0' + CEND, end=' ')

def print_canvas(canvas):
    for row in canvas:
        print('\n')
        for pixel in row:
            print_byte(pixel)
    print('\n\n\n\n')
    

def str_to_hex(string): return hex(int(string, 16))

def test_byte(byte):
    while 1:
        if int(byte, 16) >= 0:
            if int(byte, 16) <= 255:
                print("Good")
                return byte
            if int(byte, 16) > 255:
                print("Too high.")
                byte = '0xff'
        if int(byte, 16) < 0:
            print("Too low")
            byte = '0xff'

canvas = [
    ['0xff', '0xff', '0xff', '0xff'],
    ['0xff', '0xff', '0xff', '0xff'],
    ['0xff', '0xff', '0xff', '0xff'],
    ['0xff', '0xff', '0xff', '0xff'],
]


while 1:
    location = [0, 0]
    for row in canvas:
        for pixel in row:
            pixel = '0x' + input("\nPixel is currently: "+ f'{pixel}'+"  ")
            if pixel == '0x': pixel = str_to_hex('0xff')
            pixel = test_byte(pixel)
            print(location)
            read_byte(pixel, canvas, location)
            location[0] += 1
        location[0] = 0
        location[1] += 1
    
    
    print_canvas(canvas)
