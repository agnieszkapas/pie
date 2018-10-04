class Brownie(object):
    sugar = 20
    flower = 0.2
    eggs = 3
    chocolate = 1

    def __init__(self, sugar, flower, eggs, chocolate):
        self.sugar = sugar
        self.flower = flower
        self.eggs = eggs
        self.chocolate = chocolate

        self.mix()
        self.knead()
        self.bake()
        self.do_chocolate()

    def mix(self):
        print("Mixing " + str(self.eggs) + " eggs, " + str(self.flower) + " of flower, " + str(self.sugar)
              + " of sugar.")

    def knead(self):
        print("Kneading " + str(self.eggs) + " eggs, " + str(self.flower) + " of flower, " + str(self.sugar)
              + " of sugar.")

    def bake(self):
        print("Baking " + str(self.eggs) + " eggs, " + str(self.flower) + " of flower, " + str(self.sugar)
              + " of sugar.")

    def do_chocolate(self):
        print("At the end add " + str(self.chocolate) + " chocolate.")
