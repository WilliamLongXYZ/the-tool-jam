from gen import randex

import random


br = '\n\n'
geographical_feature_dict = {}


settlement_information = []


def generate_settlement(race_list, feature_list, politics_list):
    races, diversity = generate_racial_diversity(race_list)
    local_geography = generate_local_geography(feature_list)
    present_politics = generate_political_affiliations(politics_list)

def determine_races(amount, possible):
    races = []
    for i in range(0, amount):
        amount-=1
        race_num = random.randint(0, amount+1)
        if race_num >= len(possible): race_num = len(possible)-1
        race = possible[race_num]
        possible.remove(race)
        races.append(race)
    return races

def generate_local_geography(feature_list, feature_dict = geographical_feature_dict):
    # TODO: shops +feature
    # TODO: people +feature
    # TODO: create function for users to add their own geographical features +feature
    for feature in feature_list:
        feature_locations = {"Inside": False, "North": False, "East": False, "South": False, "West": False, }
        feature_present = randex.randbool()
        feature_dict[feature] = feature_present
        if feature_present:
            feature_dict[feature] = feature_locations
            for location, value in feature_dict[feature].items():
                feature_dict[feature][location] = randex.randbool()

    settlement_information.append(geographical_feature_dict)
    return geographical_feature_dict

def generate_racial_diversity(race_list):
    races_present_amnt = random.randint(1, 3)
    races = race_list.copy()
    races_present = determine_races(races_present_amnt, races)
    total_percentage = 100
    racial_diversities = []
    for i in range(0, len(races_present)):
        if i+1 >= len(races_present):
            racial_diversity = total_percentage
        if i+1 < len(races_present):
            racial_diversity = random.randint(1, total_percentage)
        racial_diversities.append(racial_diversity)
        if total_percentage > racial_diversity: total_percentage -= racial_diversity 

    settlement_information.append(races_present)
    settlement_information.append(racial_diversities)
    return races_present, racial_diversities

def generate_political_affiliations(politic_types):
    affiliations_present_amnt = len(politic_types)
    affiliations = politic_types.copy()
    affiliations_present = politic_types.copy()
    total_percentage = 100
    affiliation_percentages = []
    for i in range(0, len(affiliations_present)):
        if i+1 >= len(affiliations_present):
            affiliation_percentage = total_percentage
        if i+1 < len(affiliations_present):
            affiliation_percentage = random.randint(1, total_percentage)
        affiliation_percentages.append(affiliation_percentage)
        if total_percentage > affiliation_percentage: total_percentage -= affiliation_percentage 

    settlement_information.append(affiliation_percentages)
    return affiliation_percentages

def print_settlement():
    for i in settlement_information:
        print(i)
    print(br)

def main():
    geographical_features = {}
    geographical_feature_locations = {}

    races = input("What races would you like to have the possiblity of being included in your settlement? Seperate each with a comma.   ")
    race_list = races.split(',')
    
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
    for x in range(0, ammount):
        generate_settlement(race_list, geographical_feature_list, political_affiliations)
        print_settlement()
        settlement_information = []
    input("Press the enter key to close.")
