import random

# TODO: Name generator +feature
br = '\n\n'
sex_list = ["Male", "Female"]
global character_info
character_info = []

def generate_character(races, styles, occupations, parties):
    race = generate_race(races)
    style = generate_fighting_style(styles)
    sex = generate_sex()
    occupation = generate_occupation(occupations)
    party = generate_political_affiliation(parties)

    return race, style, sex, occupation, party

def print_character_information(character_info):
    for i in character_info:
        print(i)
    print(br)

def generate_race(races):
    chosen_race = random.choice(races)

    character_info.append(chosen_race)
    return chosen_race

def generate_fighting_style(styles):
    chosen_style = random.choice(styles)

    character_info.append(chosen_style)
    return chosen_style

def generate_sex():
    character_sex = random.choice(sex_list)

    character_info.append(character_sex)
    return character_sex

def generate_occupation(occupations):
    character_occupation = random.choice(occupations)

    character_info.append(character_occupation)
    return character_occupation

def generate_political_affiliation(parties):
    political_affiliation = random.choice(parties)

    character_info.append(political_affiliation)
    return political_affiliation





def main():
    political_affiliations = input("What political affiliations do you want your character(s) to possibly be able to have? Seperate each item with a comma.     ")
    political_party_list = political_affiliations.split(',')
    print(br)
    occupations = input("What occupations do you want your character(s) to possibly be able to have? Seperate each item with a comma.   ")
    occupation_list = occupations.split(',')
    print(br)
    races = input("What races do you want your character(s) to have to possibly be able to have? Seperate each item with a comma.   ")
    race_list = races.split(',')
    print(br)
    fighting_styles = input("What fighting styles do you want your character(s) to possibly be able to have? Seperate each item with a comma.   ")
    style_list = fighting_styles.split(',')
    print(br)
    global character_info
    characters = int(input("How many characters would you like to generate? Input any integer greater than or equal to one.     "))
    for x in range(0, characters):
        generate_character(race_list, style_list, occupation_list, political_party_list)
        print_character_information(character_info)
        character_info = []
    input("Press ENTER to continue.")
