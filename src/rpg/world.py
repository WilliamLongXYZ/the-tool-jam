import random


print(__name__)

race_list = [
    "dwarf", "elf", "human"
    ]
geographical_feature_list = [
    "mountains", "lakes", "rivers", "valleys"
    ]
geographical_feature_dict = {}
mountain_locations = {
                      "north": False,
                      "east": False,
                      "south": False,
                      "west": False}
lake_locations     = {
                      "north": False,
                      "east": False,
                      "south": False,
                      "west": False}
river_locations    = {
                      "north": False,
                      "east": False,
                      "south": False,
                      "west": False}
valley_locations   = {
                      "north": False,
                      "east": False,
                      "south": False,
                      "west": False}
settlement_information = []


for feature in geographical_feature_list:
    geographical_feature_dict[feature] = None


def rand_bool(): return bool(random.getrandbits(1))

def generate_settlement():
    races, diversity = generate_racial_diversity()
        
    local_geography = generate_local_geography()

        
    '''
    political affiliations
    '''

def determine_races(amount, possible=race_list):
    races = []
    for i in range(0, amount):
        amount-=1
        race_num = random.randint(0, amount+1)
        if race_num >= len(possible): race_num = len(possible)-1
        race = possible[race_num]
        possible.remove(race)
        races.append(race)
    return races

def generate_local_geography(geographical_features = geographical_feature_list, feature_dict = geographical_feature_dict):
    for feature in geographical_feature_list:
        feature_locations = {"North": False, "East": False, "South": False, "West": False, }
        feature_present = rand_bool()
        feature_dict[feature] = feature_present
        if feature_present:
            feature_dict[feature] = feature_locations
            for location, value in feature_dict[feature].items():
                feature_dict[feature][location] = rand_bool()

    settlement_information.append(geographical_feature_dict)
    return geographical_feature_dict

def generate_racial_diversity():
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
        total_percentage -= racial_diversity

    settlement_information.append(races_present)
    settlement_information.append(racial_diversities)
    return races_present, racial_diversities

def print_settlement():
    for i in settlement_information:
        print(i)


generate_settlement()
print_settlement()
