# from gen import randex
import randex

import random


br = '\n\n'
settlement_information = []


def generate_settlement(race_list, feature_list, feature_dict, politics_list):
    # TODO: shops +feature
    # TODO: people +feature
    races = generate_racial_diversity(race_list)
    local_geography = generate_local_geography(feature_list, feature_dict)
    present_politics = generate_political_affiliations(politics_list)

def determine_races(amount, possible):
    races = []
    for i in range(amount):
        race_num = random.randint(0, amount+1)                      # Choose a random number from the list
        if race_num >= len(possible): race_num = len(possible)-1    # Make sure the number is not too large
        race = possible[race_num]                                   # Turn the number into a race
        possible.remove(race)                                       # Prevent repeats
        races.append(race)                                          # Add race to new list
    return races

def generate_local_geography(feature_list, feature_dict):
    for feature in feature_list:
        feature_locations = {"Inside": False, "North": False, "East": False, "South": False, "West": False, }
        feature_present = randex.randbool()
        feature_dict[feature] = feature_present
        if feature_present:
            feature_dict[feature] = feature_locations
            for location, value in feature_dict[feature].items():
                feature_dict[feature][location] = randex.randbool()

    return feature_dict

def generate_racial_diversity(race_list):
    race_list = race_list.copy()
    races_present = determine_races(random.randint(1, len(race_list)), race_list)
    total_percentage = 100
    racial_diversities = []
    for i in range(len(races_present)):
        if i+1 >= len(races_present):
            racial_diversity = total_percentage
        else:
            racial_diversity = random.randint(1, total_percentage)
        racial_diversities.append(racial_diversity)
        if total_percentage > racial_diversity: total_percentage -= racial_diversity 

    return races_present, racial_diversities

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
            affiliation_percentage = random.randint(1, total_percentage)
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

    races = input("What races would you like to have the possiblity of being included in your settlement? Seperate each with a comma.   ")
    race_list = races.split(',')
    input(race_list)
    print(br)
    
    politics = input("What forms of political affiliations would you like to have the possiblity of being included in your settlement? Seperate each with a comma.  ")
    political_affiliations = politics.split(',')
    
    print(br)

    geography = input("What features would you like to have the possiblility of being included in the geography around your settlement? Seperate each with a comma.     ")
    geographical_feature_list = geography.split(',')
    for feature in geographical_feature_list:
        geographical_feature_dict[feature] = None
        geographical_feature_locations[feature] = {"inside": False, "north": False, "east": False, "south": False, "west": False}
    

    ammount = int(input("How many settlements would you like to generate? Enter an integer greater than or equal to one.    "))
    print(br)
    global settlement_information
    for x in range(ammount):
        input(race_list)
        generate_settlement(race_list, geographical_feature_list, geographical_feature_dict, political_affiliations)
        print_settlement()
        settlement_information = []
    input("Press ENTER to continue.")

# while True: generate_racial_diversity(["human", "dragon", "elf", "demon", "dwarf", "angle"])
# main()

test = ['lorem', 'ipsum', 'dolor']
amount = 3
number = random.randint(0, 2)
l = [i for i in test if i != test[number]]
print(l)

'''
races = []
for i in range(amount):                                      # HAVE
    race_num = random.randint(0, amount+1)                   # NEED          # Choose a random number from the list
    if race_num >= len(possible): race_num = len(possible)-1 # NEED          # Make sure the number is not too large
    race = possible[race_num]                                # NEED          # Turn the number into a race
    possible.remove(race)                                    # NEED          # Prevent repeats
    races.append(race)                                       # NEED
'''
