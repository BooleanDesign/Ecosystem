#Imports#
import matplotlib.pyplot as plt
import random as r

#Arbitrary Definitions#
def printanimals(orgs):
    for organism in orgs:
        print organism.name,organism.reproductive_coefficient,organism.prey,organism.population,organism.litter_size
    return None
def new_organism(orgs):
    """
    This creates a new organism
    :var orgs: Current organisms
    :return: The organism
    """
    new_loop = False # Governs the entire function process
    while new_loop is False:
        new_loop = True
        org_name = raw_input('Name: ')
        repro_loop = False
        while repro_loop is False:
            try:
                repro_loop = True
                rep_coef = float(raw_input('% Reproductive success per couple: '))
            except ValueError:
                print "Error 0201: Reproductive percent must be a float or integer."
                repro_loop = False
        """
        Works through Prey system
        """




#Main Definitions#
class Animal():
    """
    This Class defines all animals in the model
    """
    def __init__(self,name,reproductive_coefficient,prey,population,litter_size):
        """

        :param name: Name of the organism
        :param reproductive_coefficient: This determines the reproductive success
        :param prey: What does this organism eat?
        :return: self
        """
        self.litter_size = litter_size
        self.population = population
        self.name = name
        self.reproductive_coefficient = reproductive_coefficient
        self.prey = prey


    def kill(self,n):
        """
        Kills n organisms
        :param n: Number of organisms to kill off
        :return: none
        """
        self.population += -n
        return n

    def reproduce(self):
        reproductive_change = 0
        for mating_pair in range(int(self.population/2)): #compresses the organisms into mating pairs
            if r.uniform(0,100) <= self.reproductive_coefficient: #Checks if each mating pair will reproduce
                self.population += self.litter_size #adds the correct litter size to the population
                reproductive_change += self.litter_size
            else:
                pass
        return reproductive_change

def setup():
    """
    This sets up all of the animals in the ecosystem
    :return: Animals list
    """
    organisms = []
    setup_masterloop = False
    while setup_masterloop is False:
        printanimals(organisms)
        print 'All organisms must be added from producer to consumer.'
        options_loop = False # Governs The Options Menu
        while options_loop is False:
            try:
                options_loop = True
                option = raw_input('<new,delete,continue,exit>? ')
                if option != 'new' and option != 'delete' and option != 'continue' and option != 'exit':
                    raise ValueError()
                else:
                    pass
            except ValueError:
                print "Error 1001: Option input failed"
                options_loop = False
            if option == 'new':
                """
                Creating a new organism
                """
                organisms.append(new_organism())
            elif option == 'delete':
                """
                Removing an Organism
                """
                deleted_organism = raw_input('What organism would you like to remove? ')
                for organism in organisms:
                    if organism.name == deleted_organism:
                        organisms.remove(organism)
                        break
                    else:
                        pass
            elif option == 'continue':
                setup_masterloop = True
            elif option == 'exit':
                exit()
    return organisms


