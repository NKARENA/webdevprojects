import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'ormproject1.settings')
import django
django.setup()

from testapp.models import *
from faker import Faker
from random import * 
fake = Faker()

def populate(n):
    for i in range(n):
        feno= randint(1,10000)
        fename = fake.name()
        fesal = randint(10000,500000)
        feaddr = fake.city()
        emp_record = Employee.objects.get_or_create(eno=feno, ename=fename, esal=fesal, eaddr=feaddr)
        
n = int(input('Enter number of records to be created: '))
populate(n)
print(f'{n} records created successfully!')
