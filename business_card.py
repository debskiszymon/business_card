from faker import Faker
fake = Faker()

#Personal card class
class BaseContact:
    def __init__(self, first_name, last_name, email, phone_number):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.phone_number = phone_number
       
    def __str__(self):
        return f'{self.first_name} {self.last_name} {self.email} {self.phone_number}'

    def __repr__(self):
        return f"BaseContact(first_name={self.first_name}, last_name={self.last_name}, email={self.email} phone_number={self.phone_number})"

    def contact(self):
        return print(f"Wybieram {self.phone_number} i dzwonie do {self.first_name} {self.last_name}")

    @property
    def name_lenght(self):
        return len(self.first_name + " " + self.last_name)

#Business card inheritance class
class BusinessContact(BaseContact):
    def __init__(self, position, company, business_phone, business_email, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.position = position
        self.company = company
        self.business_phone = business_phone
        self.business_email = business_email

    def __repr__(self):
        return f"BusinessContact(first_name={self.first_name}, last_name={self.last_name}, email={self.email} phone_number={self.phone_number}, position={self.position}, company={self.company}, business_phone={self.business_phone}, business_email={self.business_email})"

#name1 = BaseContact("Szymon", "Debski", "debski", 600)
#name2 = BusinessContact(first_name="Gosia", last_name="Misiura", email="gosia@email.pl", phone_number="500500500", position="Dyrektor", company="Loreal", business_phone="600600600", business_email="gosia.biz@email.pl")
#print(name1)

#fake card creator function
def create_contacts():
    type = input("Wpisz rodzaj wizytowki (base_contact or business_contact): ").lower()
    if type == "base_contact" or type == "business_contact":
        try:
            quantity = int(input("Wpisz ile chcesz wygenerować wizytowek: "))
        except ValueError:
            print("Proszę podać liczbe!!")
            exit(1)
        list_base_contact = []
        list_busniess_contact = []
        if type == "base_contact":
            for i in range(quantity):
                list_base_contact.append(BaseContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.ascii_email(), phone_number=fake.msisdn()))
            for name in list_base_contact:
                print("{}, {}, {}, {}".format(name.first_name, name.last_name, name.email, name.phone_number))
            return list_base_contact
        elif type == "business_contact":
            for i in range(quantity):
                list_busniess_contact.append(BusinessContact(first_name=fake.first_name(), last_name=fake.last_name(), email=fake.ascii_email(),
                phone_number=fake.msisdn(), position=fake.job(), company=fake.company(), business_phone=fake.msisdn(), business_email=fake.ascii_company_email()))
            for name in list_busniess_contact:
                print("{}, {}, {}, {}, {}, {}, {}, {}".format(name.first_name, name.last_name, name.email, name.phone_number, name.position, name.company, name.business_phone, name.business_email))
            return list_busniess_contact
    else:
        print("Prosze podac poprawna komende")
        exit(1)
   
#create_contacts()
for z in create_contacts():
    print(z.name_lenght)


