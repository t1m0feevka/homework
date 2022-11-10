class Vehicle():
    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def increase_speed(self):
        pass

    def break_speed(self):
        pass

    def mileage_info(self):
        pass


class Bus(Vehicle):
    def __init__(self, max_speed, mileage):
        super().__init__(max_speed, mileage)

    def seating_capacity(self):
        pass


print(issubclass(Bus, Vehicle))


class SchoolBus(Bus):
    pass


print(issubclass(SchoolBus, Vehicle))
print(issubclass(SchoolBus, Bus))


class School():
    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def school_address(self):
        pass

    def main_subject(self):
        pass
