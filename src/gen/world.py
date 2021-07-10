from random import randint
from gen.randex import randbool

def generate_settlement(races_possible, politics_possible, feature_dict):
    # TODO: shops +feature
    # TODO: people +feature
    races_present, race_percentage = generate_diversity(races_possible)
    politics_present, politic_percentage = generate_diversity(politics_possible)
    local_geography = generate_local_geography(feature_dict)
    return races_present, race_percentage, politics_present, politic_percentage, local_geography

def determine_present(possible):
    possible = possible.copy()
    present = []
    amnt = randint(1, len(possible))
    for i in range(amnt):
        n = randint(0, amnt+1)
        present.append(possible[n if n < len(possible) else len(possible) -1])
        possible.remove(possible[n if n < len(possible) else len(possible) -1])
    return present

def generate_diversity(possible):
    total_percent = 100
    percentages = []
    present = determine_present(possible)
    for i in range(len(present)):
        diversity = total_percent if i+1 >= len(present) else randint(1, total_percent)
        percentages.append(diversity)
        if total_percent > diversity: total_percent -= diversity
    return present, percentages

def generate_local_geography(feature_dict):
    for feat in feature_dict:
        feature_dict[feat] = randbool()
        if feature_dict[feat]:
            feature_dict[feat] = {"Inside": False, "North": False, "East": False, "South": False, "West": False}
            for loc in feature_dict[feat]: feature_dict[feat][loc] = randbool()
    return feature_dict

def print_settlement(settlement):
    print(f'\n')
    for i in settlement:
        print(f'{i}\n')

def main():
    races = input(f'\n\nWhat races would you like to have the possiblity of being included in your settlement? Seperate each with a comma.   ')# 141 chars excluding comment
    races_possible = races.split(',')
    politics = input(f'\nWhat forms of political affiliations would you like to have the possiblity of being included in your settlement? Seperate each with a comma.  ')# 168 chars excluding comment
    politics_possible = politics.split(',')
    geo = input(f'\nWhat features would you like to have the possiblility of being included in the geography around your settlement? Seperate each with a comma.     ')# 172 chars excluding comment
    geo_dict = dict([x, None] for x in geo.split(","))
    ammount = int(input(f'\nHow many settlements would you like to generate? Enter an integer greater than or equal to one.    '))
    for x in range(ammount):
        print_settlement(generate_settlement(races_possible, politics_possible, geo_dict))
    input(f'Press ENTER to continue. ')
