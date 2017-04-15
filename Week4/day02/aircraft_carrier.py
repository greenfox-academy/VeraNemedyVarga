class Aircraft():
    def __init__(self, base_damage, max_ammo, aircraft_type):
        self.current_ammo = 0
        self.base_damage = base_damage
        self.max_ammo = max_ammo
        self.aircraft_type = aircraft_type
        self.damage = self.base_damage * self.current_ammo

    def fight(self):
        self.current_ammo = 0
        return self.damage

    def refill(self, ammo_input):
        self.ammo_input = ammo_input
        if ammo_input < self.max_ammo:
            current_ammo += ammo_input
            return 0
        else:
            current_ammo = self.max_ammo
            return ammo_input - self.max_ammo

    def get_type(self):
        return self.aircraft_type

    def get_status(self):
        return str(self.aircraft_type) + " " + str(self.current_ammo) + " " + str(self.base_damage) + " " + str(self.damage)

class F16(Aircraft):
    def __init__(self):
        super().__init__(max_ammo = 8, base_damage = 30, aircraft_type = "F16")

class F35(Aircraft):
    def __init__(self):
        super().__init__(max_ammo = 12, base_damage = 50, aircraft_type = "F35")

class Carrier():
    def __init__(self, current_carrier_ammo, health_point):
        self.current_carrir_ammo = current_carrier_ammo
        self.aircraft_list = []
        self.health_point = health_point

    def add_aircraft(self, aircraft_type):
        if aircraft_type == "f16":
            self.aircraft_list.append(F16())
        elif aircraft_type == "f35":
            self.aircraft_list.append(F35())


f16 = F16()
f35 =  F35()
carrier = Carrier(0, 0)
print(f16.base_damage)
print(f35.max_ammo)
print(f16.get_type())
print(f16.refill(10))
print(f16.get_status())
carrier.add_aircraft("f16")
carrier.add_aircraft("f35")
print(carrier.aircraft_list[0].get_type())
print(carrier.aircraft_list[1].get_type())
