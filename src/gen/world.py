from random import randint

# from gen import randex
import randex

br = '\n\n'
settlement_information = []


def generate_settlement(race_list, feature_dict, politics_list):
    # TODO: shops +feature
    # TODO: people +feature
    races = generate_racial_diversity(race_list)
    local_geography = generate_local_geography(feature_dict)
    present_politics = generate_political_affiliations(politics_list)

def determine_races(possible):
    races = []
    amnt = randint(1, len(possible))
    for i in range(amnt):
        n = randint(0, amnt+1)
        races.append(possible[n if n < len(possible) else len(possible) -1])
        possible.remove(possible[n if n < len(possible) else len(possible) -1])
    return races

def generate_racial_diversity(race_list):
    percent_t = 100
    percentages = []
    present = determine_races(race_list)
    for i in range(len(present)):
        race_div = percent_t if i+1 >= len(present) else randint(1, percent_t)
        percentages.append(race_div)
        if percent_t > race_div: percent_t -= race_div 
    return present, percentages

def generate_local_geography(feat_dic):
    for feat in feat_dic:
        feat_dic[feat] = randex.randbool()
        if feat_dic[feat]:
            feat_dic[feat] = {"Inside": False, "North": False, "East": False, "South": False, "West": False}
            for loc in feat_dic[feat]: feat_dic[feat][loc] = randex.randbool()
    return feat_dic

def generate_political_affiliations(politic_types):
    affiliations_present_amnt = len(politic_types)
    affiliations = politic_types.copy()
    affiliations_present = politic_types.copy()
    total_percentage = 100
    affiliation_percentages = []
    for i in range(len(affiliations_present)):
        if i+1 >= len(affiliations_present):
            affiliation_percentage = total_percentage
        if i+1 < len(affiliations_present):
            affiliation_percentage = randint(1, total_percentage)
        affiliation_percentages.append(affiliation_percentage)
        if total_percentage > affiliation_percentage: total_percentage -= affiliation_percentage 

    return affiliation_percentages

def print_settlement():
    for i in settlement_information:
        print(i,'\n')

def main():
    geographical_features = {}
    geographical_feature_dict = {}
    geographical_feature_locations = {}

    races = input(f'\n\n\nWhat races would you like to have the possiblity of being included in your settlement? Seperate each with a comma.   ')
    race_list = races.split(',')
    print(br)
    
    politics = input(f'What forms of political affiliations would you like to have the possiblity of being included in your settlement? Seperate each with a comma.  ')
    political_affiliations = politics.split(',')
    
    print(br)

    geography = input(f'What features would you like to have the possiblility of being included in the geography around your settlement? Seperate each with a comma.     ')
    geographical_feature_list = geography.split(',')
    for feature in geographical_feature_list:
        geographical_feature_dict[feature] = None
        geographical_feature_locations[feature] = {"inside": False, "north": False, "east": False, "south": False, "west": False}

    ammount = int(input(f'How many settlements would you like to generate? Enter an integer greater than or equal to one.    '))
    print(br)
    global settlement_information
    for x in range(ammount):
        generate_settlement(race_list, geographical_feature_dict, political_affiliations)
        print_settlement()
        settlement_information = []
    input(f'Press ENTER to continue. ')
