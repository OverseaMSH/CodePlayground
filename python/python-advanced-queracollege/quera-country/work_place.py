class WorkPlaceIsFull(Exception):

    def __str__(self):
        return "work place is full!"


class Consts:

    BASE_PRICE = {'mine': 150, 'school': 100, 'company': 90}


class WorkPlace:
    instances = []

    def __init__(self, name: str):
        self.name = name
        self.level = 1
        self.expertise = ""
        self.employees = []
        self.capacity = 1
        WorkPlace.instances.append(self)

    def get_price(self) -> int:
        return Consts.BASE_PRICE[self.expertise]

    def calc_costs(self):
        pass

    def calc_capacity(self):
        pass

    def upgrade(self):
        self.level += 1
        self.calc_capacity()

    def hire(self, person):
        if len(self.employees) >= self.capacity:
            raise WorkPlaceIsFull()
        self.employees.append(person)
        person.work_place = self

    def get_expertise(self) -> str:
        return self.expertise

    def calc(self) -> int:
        return -1 * self.calc_costs()

    @staticmethod
    def calc_all() -> int:
        total = 0
        for workplace in WorkPlace.instances:
            total += workplace.calc()
        return total
