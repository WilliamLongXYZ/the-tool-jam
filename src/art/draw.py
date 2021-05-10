print(__name__)

hex_bytes = ['0x00']
print(0xff)
CEND = '\33[0m'

CBLACK = '\033[30m'
CRED = '\033[91m'
CWHITE = '\033[37m'


def read_byte(byte):
    pass

def print_byte(byte):
    if byte == '0x00':
        print(CBLACK + byte + CEND)
    if byte == '0x80':
        print(CRED + byte + CEND)
    if byte == '0xff':
        print(CWHITE + byte + CEND)
    

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
    for row in canvas:
        input("Row (start): " + f'{row}')
        for pixel in row:
            pixel = '0x' + input("Pixel is currently: "+ f'{pixel}'+"  ")
            if pixel == '0x': pixel = str_to_hex('0xff')
            pixel = test_byte(pixel)
            print_byte(pixel)
        input("Row (end): " + str(row) + "\n\n\n")
    input(canvas)
