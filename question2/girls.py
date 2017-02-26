class Girl:

    def __init__(self,name,attribute,intelligence,budget,typ):
        self.name = name
        self.attribute = attribute
        self.intelligence = intelligence
        self.budget = budget
        self.status = 'single'
        self.bf_name = ''
        self.happiness = 0
        self.type = typ

    def is_elligible(self,gf_bud):
        if (self.budget <= gf_bud):
            return True
        else:
            return False
