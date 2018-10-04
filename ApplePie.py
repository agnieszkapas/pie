class ApplePie(object):
    sugar = 10
    flower = 0.5
    eggs = 2

    def __init__(self, sugar, flower, eggs):
        self.sugar = sugar
        self.flower = flower
        self.eggs = eggs

        self.masa_jaja = 10

        self.mix()
        self.knead()
        self.bake()

    def mix(self):
        print("Mixing " + str(self.eggs) + " eggs, " + str(self.flower) + " of flower, " + str(self.sugar)
              + " of sugar.")

    def knead(self):
        print("Kneading " + str(self.eggs) + " eggs, " + str(self.flower) + " of flower, " + str(self.sugar)
              + " of sugar.")

    def bake(self):
        print("Baking " + str(self.eggs) + " eggs, " + str(self.flower) + " of flower, " + str(self.sugar)
              + " of sugar.")

    def weight(self):
        mass = ((self.sugar + self.flower + (self.eggs * self.masa_jaja)) / 100)
        print("The pies mass is " + str(round(mass, 2)) + "kg")

