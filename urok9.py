#1 klass - shablon
#2 obekt - zapolneniy shablon
#3 metod - funksiya klassa
#4 atribut - xaraktera

class Sayt:
    def __init__(self, username, text, likes=0):
        self.username = username
        self.text = text
        self.likes = likes


saytchi = Sayt('username', 'good job')


class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def stop(self):
        print(f'{self.model} ostanovilas')


gentra = Car('ravon', 'black', 2022)  # snachala sozdal ekzemplyar


class Car:
    def __init__(self, model, color, year):
        self.model = model
        self.color = color
        self.year = year

    def stop(self):
        print('mashina ostanovilas')

    def change_color(self, new_color):
        self.color = new_color


gentra = Car('ravon', 'black', 2022)  # snachala sozdal ekzemplyar
gentra.change_color('white')
gentra.stop()


class Bankakk:
    def __init__(self, imya, balance=0.0):
        self.imya = imya
        self.balance = balance

    def deposit(self, summa):
        self.balance = self.balance + summa
        print(f'Balans popolnen na {summa}')

    def cash(self, summa):
        if self.balance >= summa:
            self.balance = self.balance - summa
            print(f'balansa snyata {summa}')
        else:
            print('nedostatochna sredstv')

    def show(self):
        print(f'balans polzavetlya {self.imya} raven {self.balance}sum')


bank_user = Bankakk(imya=input('vvedite imya: '))
while True:
    menu = input('viberite punkt menyu: \n'
                     '1 vash balans \n'
                     '2 popolnit balans \n'
                     '3 snyat dengi: ')

    if menu == '1':
        bank_user.show()
    elif menu == '2':
        summa = input('vvedite dengi: ')
        bank_user.deposit(int(summa))
    elif menu == '3':
        summa = input('skolka snyat?: ')
        bank_user.cash(int(summa))
    else:
        print('net takoy funksi')