import random
from gen.randex import randfloat

# TODO: galaxy +feature
# TODO: planets +feature

def generate_star(masses=None, min = 0, max = 20):
    masses = randfloat(min, max) if masses == None else float(masses)
    luminosity = masses**4
    diameter = masses**0.74
    return masses, luminosity, diameter

def print_info(info):
    for i in info:
        print(f'{i}\n')

def main():
    number = int(input("How many stars would you like to generate?    "))
    for x in range(0, number):
        star_mass = input("What is the mass of your star? Default is random.    ")
        if star_mass == '':
            min_max = input("What are the minimum and maximum masses you want your star to be? Seperate with a comma, defaults are zero and twenty.    ").split(',')
            star = generate_star() if min_max == [''] else generate_star(None, float(min_max[0]), float(min_max[1]))
        if star_mass != '': star = generate_star(star_mass)
        print_info(star)
