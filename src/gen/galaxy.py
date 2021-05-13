from gen import functions as randex

import random


print(__name__)

def generate_star_system():
    generate_star()

def generate_star():
    solar_masses = randex.randfloat(0, 20)
    luminosity = solar_masses**4
    diameter = solar_masses**0.74
    surface_temperature = solar_masses**0.505
    lifetime = solar_masses**-2.5
    inner_habitable_zone = lifetime**0.5 * 0.95
    outer_habitable_zone = lifetime**0.5 * 1.37
    inner_zone = solar_masses * 0.1 # AU
    outer_zone = solar_masses * 40 # AU
    frost_line = 4.85*luminosity**0.5 # Location in AU
    print(solar_masses,
          luminosity,
          diameter,
          surface_temperature,
          lifetime,
          inner_habitable_zone,
          outer_habitable_zone)

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

generate_star_system()
