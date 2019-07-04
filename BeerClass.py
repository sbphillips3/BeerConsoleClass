#!/usr/bin/env python3
# @author Sean Phillips
# A basic class and main method that creates a Beer object with 3 parameters and
# in the main 3 beer objs are created and then called with a beer_print function
# in the console

class Beer:
    def __init__(self, beer, beer_type, percent):
        self._beer = beer
        self._beer_type = beer_type
        self._percent = percent

    def beer(self):
        return self._beer

    def beer_type(self):
        return self._beer_type

    def percent(self):
        return self._percent

# method print_header() prints a header for the beers printed
def print_header():
    print('-----------------------------------------------------------------------')
    print('Beer                       |   Type             |    ABV')
    print('-----------------------------------------------------------------------')

# method print_beer(beer) checks object to make sure it is a beer, if it is
# it is then printed in a formatted string to the console
# @params beer
def print_beer(beer):
    if not isinstance(beer, Beer):
        raise TypeError('print_beer(): requires a Beer as the type')
    print('{}    |   {}    |    {}%' .format(beer.beer(), beer.beer_type(), beer.percent()))
    print('-----------------------------------------------------------------------')
    
# main method
def main():

    beer1 = Beer('Blvd Jam Band Berry Ale', 'Fruit Ale    ', 5.9)
    beer2 = Beer('Blvd Pale Ale          ', 'Amer Pale Ale', 5.4)
    beer3 = Beer('Blvd Space Camper      ', 'IPA          ', 5.9)

    # beer objects put into a list
    beerList = {beer1, beer2, beer3}

    print_header()

    for b in beerList:
        print_beer(b)

if __name__ == '__main__': main()
