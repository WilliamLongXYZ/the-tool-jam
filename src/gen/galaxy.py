import random
from gen.randex import randfloat

def generate_star_system(solar_masses=None, min_sm = 0, max_sm = 20):
    generate_star()

def generate_star(solar_masses=None, min_sm = 0, max_sm = 20):
    if solar_masses == None:
        solar_masses = randfloat(min_sm, max_sm)
    solar_masses = float(solar_masses)
    luminosity = solar_masses**4
    diameter = solar_masses**0.74
    surface_temperature = solar_masses**0.505
    lifetime = solar_masses**-2.5
    inner_habitable_zone = lifetime**0.5 * 0.95
    outer_habitable_zone = lifetime**0.5 * 1.37
    inner_zone = solar_masses * 0.1 # AU
    outer_zone = solar_masses * 40 # AU
    frost_line = 4.85*luminosity**0.5 # Location in AU

def generate_terrestrial():
    pass

def generate_galaxy():
    pass
    '''
    star system location:
        within galactic plane
        within spiral galaxy
        1/2 - 2/3 out from center
        not in the arms of the galaxy
    '''

def main():
    number = int(input("How many stars would you like to generate? Please enter an integer greater than or equal to one."))
    for x in range(0, number_of_stars):
        star_mass = input("What is the mass of your star? Leave blank for default of random.    ")
        if star_mass == '':
            minimum = input("What is the minimum mass you want your star to be? Default is zero.  ")
            maximum = input("What is the maximum mass you want your star to be? Default is twenty.    ")
            if maximum == '' and minimum == '':
                return generate_star()
            return generate_star(None, float(minimum), float(maximum))
        return generate_star(star_mass)
