from getpass import getpass

from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand, CommandError

User = get_user_model()

class Command(BaseCommand):
    help = "Create a normal user"

    def handle(self, *args, **options):
        username = options.get("username")
        email = options.get("email")

        if not username:
            username = input("Username: ").strip()

        if not email:
            email = input("Email: ").strip()

        if User.objects.filter(username=username).exists():
            raise CommandError("A user with this username already exists.")

        while True:
            password = getpass("Password: ")
            password2 = getpass("Password (again): ")

            if password != password2:
                self.stderr.write(
                    self.style.ERROR("Passwords do not match. Try again.")
                )
                continue

            if not password:
                self.stderr.write(
                    self.style.ERROR("Password cannot be blank.")
                )
                continue

            break

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password,
        )

        self.stdout.write(
            self.style.SUCCESS(
                f'User "{user.username}" created successfully.'
            )
        )