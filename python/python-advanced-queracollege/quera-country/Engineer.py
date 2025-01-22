from Person import Person, Consts

class Engineer(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = "engineer"

    def get_price(self):
        base_price = Consts.BASE_PRICE[self.job]
        return int(base_price * Consts.MIN_AGE / self.age)

    def calc_life_cost(self):
        base_cost = Consts.BASE_COST[self.job]
        return int(base_cost * Consts.MIN_AGE / self.age)

    def calc_income(self):
        base_income = Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]
        return int(base_income * Consts.MIN_AGE / self.age)
