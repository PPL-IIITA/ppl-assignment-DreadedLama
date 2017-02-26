class Boy:

    def __init__(self,name,attribute,intelligence,budget,min_requirement):
        self.name = name
        self.attribute = attribute
        self.intelligence = intelligence
        self.budget = budget
        self.min_requirement = min_requirement
        self.status = 'single'
        self.gf_name = ''

    def is_elligible(self,min_budget,attribute):
        if (self.budget >= min_budget) and (attribute >= self.min_requirement):
            return True
        else:
            return False
