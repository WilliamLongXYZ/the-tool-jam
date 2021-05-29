from random import choice

def generate_character(races, styles, occupations, politics):
    sex = generate_sex()
    race = generate_race(races)
    style = generate_fighting_style(styles)
    occupation = generate_occupation(occupations)
    party = generate_political_affiliation(politics)

    return race, style, sex, occupation, party

def generate_sex():
    return choice(["Male", "Female"])

def generate_race(races):
    return choice(races)

def generate_fighting_style(styles):
    return choice(styles)

def generate_occupation(occupations):
    return choice(occupations)

def generate_political_affiliation(politics):
    return choice(politics)

def print_character_information(character_info):
    for i in character_info:
        print(i)
    print(br)

def main():
    races = input("What races do you want your character(s) to have to possibly be able to have? Seperate each item with a comma.   ").split(',')
    styles = input("What fighting styles do you want your character(s) to possibly be able to have? Seperate each item with a comma.   ").split(',')
    occupations = input("What occupations do you want your character(s) to possibly be able to have? Seperate each item with a comma.   ").split(',')
    politics = input("What political affiliations do you want your character(s) to possibly be able to have? Seperate each item with a comma.     ").split(',')

    characters = int(input("How many characters would you like to generate? Input any integer greater than or equal to one.     "))
    for x in range(0, characters):
        generate_character(races, styles, occupations, politics)
    input("Press ENTER to continue.")
