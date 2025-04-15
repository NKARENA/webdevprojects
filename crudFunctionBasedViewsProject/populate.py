import os 
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'crudFunctionBasedViewsProject.settings')
import django
django.setup()

from testApp.models import *
from faker import Faker
from random import * 
fake = Faker()

def populate(n):
    for i in range(n):
        fnum= randint(1,1000)
        fename = fake.name()
        fesal = randint(10000,500000)
        feaddr = fake.city()
        emp_record = Employee.objects.get_or_create(enum=fnum, ename=fename, esal=fesal, eaddr=feaddr)
        
populate(20)
