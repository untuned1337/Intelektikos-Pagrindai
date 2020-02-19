
class Data(object):
    def __init__(self, *args):
        self.id = args[0]
        self.hours = args[1]
        self.income = args[2]
        self.age = args[3]
        self.education = args[4]
        self.child5 = args[5]
        self.child13 = args[6]
        self.child17 = args[7]
        self.nonwhite = args[8]
        self.owned = args[9]
        self.mortgage = args[10]
        self.occupation = args[11]
        self.unemployed = args[12]


class ContinuousData(object):
    def __init__(self, count, *args):
        self.count = count
        self.hours_list = args[0]
        self.income_list = args[1]
        self.age_list = args[2]
        self.education_list = args[3]
        self.child5_list = args[4]
        self.child13_list = args[5]
        self.child17_list = args[6]
        self.unemployed_list = args[7]


class CategoricalData(object):
    def __init__(self, count, *args):
        self.count = count
        self.nonwhite_list = args[0]
        self.owned_list = args[1]
        self.mortgage_list = args[2]
        self.occupation_list = args[3]
