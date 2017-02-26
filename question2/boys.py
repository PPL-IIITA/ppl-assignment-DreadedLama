class Boy:


    def __init__(self,name,attribute,intelligence,budget,min_requirement,typ):
        self.name = name
        self.attribute = attribute
        self.intelligence = intelligence
        self.budget = budget
        self.min_requirement = min_requirement
        self.status = 'single'
        self.gname = ''
        self.happiness = 0
        self.type = typ

    def is_elligible(self,min_budget,attribute):
        if (self.budget >= min_budget) and (attribute >= self.min_requirement):
            return True
        else:
            return False
