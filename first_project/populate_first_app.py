import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE','first_project.settings')
import django
django.setup()
import random
from first_app.models import User
from faker import Faker
fakegen=Faker()

def populate(N=5):
    for entry in range(N):
        #create the fake data for that entry
        fake_nom=fakegen.company()
        fake_email=fakegen.email()
        #create the new web page entry
        user=User.objects.get_or_create(first_name=fake_nom, last_name=fake_nom, email=fake_email)[0]

if __name__=='__main__':
    print('populating script')
    populate(5)
    print('population complete')
