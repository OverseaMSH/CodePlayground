from Person import Person, Consts

class Worker(Person):
    def __init__(self, name, age):
        super().__init__(name, age)
        self.job = "worker"

    def get_price(self):
        base_price = Consts.BASE_PRICE[self.job]
        return int(base_price * Consts.MIN_AGE / self.age)

    def calc_life_cost(self):
        base_cost = Consts.BASE_COST[self.job]
        return int(base_cost * self.age / Consts.MIN_AGE)

    def calc_income(self):
        base_income = Consts.BASE_INCOME[self.job][self.work_place.get_expertise()]
        return int(base_income * self.age / Consts.MIN_AGE)
