from django.core.management.base import BaseCommand, CommandError
from rent_store.models import CustomUser


class Command(BaseCommand):
    help = 'Creates a user in db'

    def add_arguments(self, parser):
        pass

    def handle(self, *args, **options):
        username = input('Enter username: ')
        email = input('Enter email: ')
        first_name = input('Enter First name: ')
        last_name = input('Enter Last name: ')
        while True:
            password = input('Enter password: ')
            password_ = input('Re-Enter password: ')
            if password == password_:
                break
            else:
                print("Passwords do not match")
        try:
            user = CustomUser.objects.create(username=username, email=email, first_name=first_name, last_name=last_name)
            user.set_password(password)
            user.save()
            print("User {} created".format(username))
        except Exception as e:
            print(e)
            print("User creation failed")