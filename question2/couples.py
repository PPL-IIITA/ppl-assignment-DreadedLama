class Couple:

    def __init__(self,boy,girl):
        self.boy = boy
        self.girl = girl
        self.happiness = 0
        self.compatibility = 0
        self.GFT = []

    def set_happiness(self):
        self.happiness = self.girl.happiness + self.boy.happiness

    def set_compatibility(self):
        a = self.boy.budget - self.girl.budget
        b = abs(self.boy.intelligence - self.girl.intelligence)
        c = abs(self.boy.attribute - self.girl.attribute)
        self.compatibility = a+b+c
