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
        return f"{self.first_name}, {self.last_name}, {self.company}, {self.position}, {self.email}"

    def __repr__(self):
        return f"nameCard(first_name={self.first_name}, last_name={self.last_name}, company={self.company}, position={self.position}, email={self.email})"

#name1 = nameCard("Szymon", "Debski", "Mercedes", "Kontroler", "debski")
#print(name1)

def fake_names():
    list= []
    for i in range(10):
        list.append(nameCard(first_name=fake.first_name(), last_name=fake.last_name(), company=fake.company(), position=fake.job(), email=fake.ascii_company_email()))
    return list

for name in fake_names():
    print("{}, {}, {}, {}, {}".format(name.first_name, name.last_name, name.company, name.position, name.email))
