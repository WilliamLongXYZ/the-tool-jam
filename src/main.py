from gen import character, world, galaxy


def info():
    print('''\n\n
    This program is my submission for the itch.io Tool Jam, and can generate a star, settlement, or character for an RPG.
    It was inspired by Artifexian on YouTube.
    You can find the source at https://github.com/Xarvveron/the-tool-jam , and you can download the tool and all updates from https://xarvveron.itch.io/generator
    ''')
    input("Press ENTER to continue.\n\n")

def main():
    while True:
        print("\n\n\nCommands:\n[character] or [c]: generate a character\n[settlement] or [town] or [t]: generate a settlement\n[star] or [s]: generate a star\n[info] or [i]: view information about this tool\n\n")

        generator = input("What would you like to generate?    ")
        if generator == 'character' or generator == 'c':
            character.main()
        if generator == 'settlement' or generator == 'town' or generator == 't':
            world.main()
        if generator == 'star' or generator == 's' or generator == 'star':
            galaxy.main()
        if generator == 'info' or generator == 'i':
            info()

main()
