class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


human1 = Person('Lisa', 16)
human2 = Person('Hannah', 19)

print('Имя:', human1.name, 'Возрaст:', human1.age)
print('Имя:', human2.name, 'Возрaст:', human2.age)


class User:
    def __init__(self, name, mail, age, phone_number):
        self.name = name
        self.mail = mail
        self.age = age
        self.phone_number = phone_number

    def change_name(self, new_name):
        self.name = new_name

    def change_mail(self, new_mail):
        self.mail = new_mail

    def change_phone_number(self, new_phone_number):
        self.phone_number = new_phone_number


chel = User('Rodrigeo', 'Rodrigeo@mail.com', 23, 123456789)
chel.change_phone_number(9113611)
print('Imya:', chel.name, 'Pochta:', chel.mail, 'Vozrast:', chel.age, 'Nomer telefona:', chel.phone_number)
