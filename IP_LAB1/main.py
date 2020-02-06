import Reader
class Data(object) :
    def __init__(self, id, hours, income, age, education, child5, child13, child17, nonwhite, owned, mortgage, occupation, unemp):
        self.id = id
        self.hours = hours
        self.income = income
        self.age = age
        self.education = education
        self.child5 = child5
        self.child13 = child13
        self.child17 = child17
        self.nonwhite = nonwhite
        self.owned = owned
        self.mortgage = mortgage
        self.occupation = occupation
        self.unemp = unemp
Reader.readFile('./Database/WorkingHours.csv')
def Min(dataArr):
    min = dataArr[0]
    for data in dataArr:
        print(5);



