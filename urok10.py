class Person:
    def login(self, qwerty):
        pass
class Mepr(Person):
    def logout(self, mpfive):
        pass


class Car:
    def __init__(self, color, year, model):
        self.car_color = color
        self.car_year = year
        self.car_model = model
    def ehat(self):
        print('mawina edet')

class Gruzovik(Car):
    def __init__(self, color, year, model, gruzopod):
        super().__init__(color, year, model)
        self.gruzopod = gruzopod
    def perevozka_gruza(self):
        print('gruzovik perevozit gruz')
    @property
    def probeg(self):
        return self.car_year+200
    @classmethod
    def info(cls, act):
        return act

kamaz = Gruzovik('black', 2005, 'man', 200)
kamaz.perevozka_gruza()
print(kamaz.probeg)
print(Gruzovik.info('proverka'))

class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

class Supercar(Car):
    def __init__(self, model, color, year, sponsor):
        super().__init__(model, color, year)
        self.sponsor = sponsor

class Parent1:
    pass
class Parent2:
    pass
class Child(Parent1, Parent2):
    pass

data_base = {}
class Worker:
    def __init__(self, name, doljnost):
        self.name = name
        self.doljnost = doljnost
        # soxranyaem dannie v bazu dannix
        data_base[self.name] = self.doljnost


class Manager(Worker):
    def __init__(self, name, doljnost):
        super().__init__(name, doljnost)
        # soxranyaem dannie v bazu dannix
        data_base[self.name] = self.doljnost

    def check_workers(self, password):
        password_check = 123
        # proveryaem pravilno li vveden parol
        if int(password) == password_check:
            return data_base
        else:
            return 'nepravilniy parol'


while True:
    menu = input('kem vi yevlyaetes')
    if menu.lower() == 'rabotnik':
        worker = Worker(input('vvedite svoe imya:'), input('vvedite doljnost'))
    if menu.lower() == 'menedjer':
        manager = Manager(input('vvedite svoe imya'), input('vvedite doljnost'))
        password = input('vvedite parol')
        print(manager.check_workers(password))


class Player:
    def __init__(self, udarit_myach, passavat):
        self.udarit_myach = udarit_myach
        self.passavat = passavat


class Napadayushiy(Player):
    def __init__(self, udarit_myach, passavat, drebling):
        super().__init__(udarit_myach, passavat)
        self.drebling = drebling
    def celebrate(self):
        return 'Празднование после забытого гола'



class Zashitnik(Player):
    def __init__(self, udarit_myach, passavat, vishiy_rost, silniy):
        super().__init__(udarit_myach, passavat)
        self.vishiy_rost = vishiy_rost
        self.silniy = silniy
    def reshayushiy(self):
        return 'Делает решающий вынос для защиты ворот в игре'


class Poluzashitnik(Player):
    def __init__(self, udarit_myach, passavat, bistro_begat):
        super().__init__(udarit_myach, passavat)
        self.bistro_begat = bistro_begat
    def assist(self):
        return 'Делает кравсивые пассы для нападающих'


class Vratar(Player):
    def __init__(self, udarit_myach, passavat, vishiy_rost, dlina_ruk, reaksiya):
        super().__init__(udarit_myach, passavat)
        self.vishiy_rost = vishiy_rost
        self.dlina_ruk = dlina_ruk
        self.reaksiya = reaksiya
    def defence(self):
        return 'Организует защиту для игры и играет важнейшую роль'