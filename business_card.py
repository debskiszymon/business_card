from faker import Faker
fake = Faker()

class nameCard:
    def __init__(self, first_name, last_name, company, position, email):
        self.first_name = first_name
        self.last_name = last_name
        self.company = company
        self.position = position
        self.email = email
       
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email}'

    def __repr__(self):
        return f"nameCard(first_name={self.first_name}, last_name={self.last_name}, company={self.company}, position={self.position}, email={self.email})"

    def contact(self):
        return print(f"Kontaktuję się z {self.first_name}, {self.last_name}, {self.position}, {self.email}")

    @property
    def name_lenght(self):
        return len(self.first_name + " " + self.last_name)

name1 = nameCard("Szymon", "Debski", "Mercedes", "Kontroler", "debski")
#print(name1)

def fake_names():
    list = []
    for i in range(10):
        list.append(nameCard(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.ascii_company_email()))
    return list

print(name1.name_lenght)

'''
name_1 = nameCard("Szymon", "Debski", "Mercedes", "Kontroler", "debski@")
name_2 = nameCard("Gosia", "Misiura", "Loreal", "Dyrektor", "gosia@")
name_3 = nameCard("Mateusz", "Debski", "Lego", "kulfon", "mati@")
list2 = [name_1, name_2, name_3]

by_first_name = sorted(list2, key=lambda name_card: name_card.first_name) 
by_last_name = sorted(list2, key=lambda name_card: name_card.last_name)
by_email = sorted(list2, key=lambda name_card: name_card.email)

for name in by_email:
    print("{}, {}, {},".format(name.first_name, name.last_name, name.email))
'''

'''
for name in fake_names():
    print("{}, {}, {}, {}, {}".format(name.first_name, name.last_name, name.company, name.position, name.email))
'''