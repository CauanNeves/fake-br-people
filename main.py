from faker import Faker

fake = Faker('pt_BR')

print(f'''
{fake.name()}
{fake.cpf()}
{fake.email()}
{fake.address()}
''')