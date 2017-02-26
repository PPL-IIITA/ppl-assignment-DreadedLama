class Girl:

    def __init__(self,name,attribute,intelligence,budget):
        self.name = name
        self.attribute = attribute
        self.intelligence = intelligence
        self.budget = budget
        self.status = 'single'
        self.bf_name = ''

    def is_elligible(self,gf_budget):
        if (self.budget <= gf_budget):
            return True
        else:
            return False
