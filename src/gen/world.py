from random import randint

from gen.randex import randbool


def generate_settlement(race_list, feature_dict, politics_list):
    # TODO: shops +feature
    # TODO: people +feature
    races, race_percentage = generate_diversity(race_list)
    politics, pol_percentage = generate_diversity(politics_list)
    local_geography = generate_local_geography(feature_dict)

    return races, race_percentage, politics, pol_percentage, local_geography

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

def generate_local_geography(feat_dic):
    for feat in feat_dic:
        feat_dic[feat] = randbool()
        if feat_dic[feat]:
            feat_dic[feat] = {"Inside": False, "North": False, "East": False, "South": False, "West": False}
            for loc in feat_dic[feat]: feat_dic[feat][loc] = randbool()
    return feat_dic

def print_settlement(settlement):
    for i in settlement:
        print(f'{i}\n')

def main():
    geographical_features = {}
    geographical_feature_dict = {}
    geographical_feature_locations = {}

    races = input(f'\n\n\nWhat races would you like to have the possiblity of being included in your settlement? Seperate each with a comma.   ')
    race_list = races.split(',')
    print(f'\n')
    politics = input(f'What forms of political affiliations would you like to have the possiblity of being included in your settlement? Seperate each with a comma.  ')
    political_affiliations = politics.split(',')
    print(f'\n')
    geography = input(f'What features would you like to have the possiblility of being included in the geography around your settlement? Seperate each with a comma.     ')
    geographical_feature_list = geography.split(',')
    for feature in geographical_feature_list:
        geographical_feature_dict[feature] = None
        geographical_feature_locations[feature] = {"inside": False, "north": False, "east": False, "south": False, "west": False}
    ammount = int(input(f'\nHow many settlements would you like to generate? Enter an integer greater than or equal to one.    '))
    for x in range(ammount):
        settlement = generate_settlement(race_list, geographical_feature_dict, political_affiliations)
        print_settlement(settlement)
    input(f'Press ENTER to continue. ')
