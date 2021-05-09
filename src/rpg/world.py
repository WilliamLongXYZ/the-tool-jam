import random


print(__name__)

race_list = ["dwarf", "elf", "human"]
geographical_feature_list = ["mountains", "lakes", "rivers", "valleys"]
geographical_feature_dict = {}
for feature in geographical_feature_list:
    geographical_feature_dict[feature] = None

def rand_bool():
    return bool(random.getrandbits(1))

def generate_settlement():
    races_present_amnt = random.randint(1, 3)
    races = race_list.copy()
    races_present = determine_races(races_present_amnt, races)
    print(races_present)
    total_percentage = 100
    for i in range(0, len(races_present)):
        if i+1 >= len(races_present):
            racial_diversity = total_percentage
            print(str(racial_diversity) + "%")
        if i+1 < len(races_present):
            racial_diversity = random.randint(1, total_percentage)
            print(str(racial_diversity) + "%")
        total_percentage -= racial_diversity
    
    local_geography = generate_local_geography()
    print(local_geography)
        
    '''
    political affiliations
    local geography
    '''

def determine_races(amount, possible=race_list):
    print(amount)
    races = []
    for i in range(0, amount):
        amount-=1
        print(i)
        race_num = random.randint(0, amount+1)
        if race_num >= len(possible): race_num = len(possible)-1
        race = possible[race_num]
        possible.remove(race)
        races.append(race)
    return races

def generate_local_geography(geographical_features = geographical_feature_list):
    for feature in geographical_feature_list:
        feature_present = rand_bool()
        print(feature, feature_present)
        geographical_feature_dict[feature] = feature_present

    return geographical_feature_dict


generate_settlement()
