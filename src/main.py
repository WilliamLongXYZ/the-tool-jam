from gen import character, world, galaxy

def main():

    print("")


    generator = input("Would you like to generate a character [character] or [c], a settlement [town] or [t] or [settlement], or a star [star] or [s]?    ")
    if generator == 'character' or generator == 'c':
        character.main()
    if generator == 'settlement' or generator == 'town' or generator == 't':
        world.main()
    if generator == 'star' or generator == 's' or generator == 'star':
        galaxy.main()
    if generator == 'info':
        info()

def info():
    print('\n\n')
    print("This program is my submission for the itch.io Tool Jam, and can generate a star, settlement, or character for an RPG.\n")
    print("You can find the source at https://github.com/Xarvveron/the-tool-jam , and you can download the tool and all updates from https://xarvveron.itch.io/world-generator")

main()
