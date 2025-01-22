from Person import Person, Consts

class Teacher(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = "teacher"

    def get_price(self):
        base_price = Consts.BASE_PRICE[self.job]
        return int(base_price - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)

    def calc_life_cost(self):
        base_cost = Consts.BASE_COST[self.job]
        return int(base_cost + (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)

    def calc_income(self):
        base_income = Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]
        return int(base_income - (self.age - Consts.MIN_AGE) * Consts.AGE_MUL)
