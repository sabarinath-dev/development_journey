"""
ObjectOrientedProgramming
class :designpattern,blueprint
object:realworld entity

self

"""

class SuperHero:

    name:str

    universe:str

    def set_super_hero(self,name,universe):

        self.name = name

        self.universe = universe

    def walk(self):

        print(self.name,"is walking")

    def run(self):

        print(self.name,"is running")

super_hero_instance1=SuperHero()

super_hero_instance1.set_super_hero("captainamerica","marvel")

super_hero_instance2=SuperHero()

super_hero_instance2.set_super_hero("batman","dc")

super_hero_instance3=SuperHero()

super_hero_instance3.set_super_hero("minnalmurali","basiluniverse")

super_hero_instance2.walk()