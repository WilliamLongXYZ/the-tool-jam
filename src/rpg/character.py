import random

print(__name__)

'''
Name generator
Sex generator
Occupation
Political Affiliation
'''

political_party_list = ["anarchist", "libertarian", "authoritarian"]
occupation_list = ["blacksmith", "soldier", "merchant"]
sex_list = ["Male", "Female"]
race_list = ["elf", "human", "cat", "mouse"]
style_list = ["one-handed", "two-handed", "dual-wield", "magic", "ranged"]
character_info = []

def generate_race(races = race_list):
    chosen_race = random.choice(races)

    character_info.append(chosen_race)
    return chosen_race

def generate_fighting_style(styles = style_list):
    chosen_style = random.choice(styles)

    character_info.append(chosen_style)
    return chosen_style

def generate_sex():
    character_sex = random.choice(sex_list)

    character_info.append(character_sex)
    return sex_list

def generate_occupation(occupations=occupation_list):
    character_occupation = random.choice(occupations)

    character_info.append(character_occupation)
    return character_occupation

def generate_political_affiliation(parties=political_party_list):
    political_affiliation = random.choice(parties)

    character_info.append(political_affiliation)
    return political_affiliation


def print_character_information(character_info):
    for i in character_info:
        print(i)


def generate_character():
    race = generate_race()
    style = generate_fighting_style()
    sex = generate_sex()
    occupation = generate_occupation()
    party = generate_political_affiliation()

    return race, style, sex, occupation, party

generate_character() 


print_character_information(character_info)
