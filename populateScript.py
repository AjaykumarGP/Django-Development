import os
os.environ.setdefault('DJANGO_SETTINGS_MODULE',
                      'DjangoDevelopement_SideProject1.settings')

import django
django.setup()

from FirstApp.models import UserInfo
from faker import Faker

def populate(quantity):
    fake = Faker()
    for i in range(0, quantity):
        user = UserInfo(firstName = fake.name(), lastName = fake.name(), email = fake.email())
        user.save()


# Start execution here!
if __name__ == '__main__':
    print("Starting UserInfo population script...")
    populate(50)
    print("Finished populating")