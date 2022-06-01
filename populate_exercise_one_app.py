import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'exercise_one.settings')

import django
django.setup()

# FAKE POPULATION SCRIPT

import random
from exercise_one_app.models import User
from faker import Faker

fake_gen = Faker()
    
def populate(N=5):
    
    for entry in range(N):
        
        name = fake_gen.name()
        
        # create fake data
        fake_first_name = name.split()[0]
        fake_last_name = name.split()[1]
        fake_email = fake_first_name + '.' + fake_last_name + '@gmail.com'
        
        #fake access AccessRecord
        user = User.objects.get_or_create(first_name=fake_first_name, last_name=fake_last_name, email=fake_email)[0]
        
if __name__ == '__main__':
    print('populating script!')
    populate(20)
    print('populating completed')
        
        