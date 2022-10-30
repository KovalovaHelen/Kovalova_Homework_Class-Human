class Human:

    def __init__(self, name, surname, age, phone, address):
        self.name = name
        self.surname = surname
        self.age = age
        self.phone = phone
        self.address = address

    def __str__(self):
        return f'{self.name} {self.surname}'

    def get_info(self):
        return {
            'name': self.name,
            'surname': self.surname,
            'age': self.age,
            'phone': self.phone,
            'address': self.address,
        }

    def call(self, phone_number):
        return f'{self.phone} вызывает абонента {phone_number}'


human1 = Human(name='Olena', surname='Kovalova', age=32, phone='+380976768557', address='Odessa, str.Mayachnaja 7')
human2 = Human(name='Andriy', surname='Kovalov', age=37, phone='+380676768557', address='Odessa, str.Mayachnaja 7')
human3 = Human(name='Timofej', surname='Kovalov', age=8, phone='+380506768557', address='Odessa, str.Mayachnaja 7')

print(human1)
print(human1.get_info())
print(human1.call('+380976768557'))

print(human2)
print(human2.get_info())
print(human2.call('+380676768557'))

print(human3)
print(human3.get_info())
print(human3.call('+380506768557'))
