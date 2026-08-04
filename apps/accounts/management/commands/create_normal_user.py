from getpass import getpass

from django.core.management.base import BaseCommand
from django.core.validators import EmailValidator
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError
from django.db import transaction
from django.contrib.auth.models import User
from apps.accounts.models import UserProfile


class Command(BaseCommand):
    help = "Create a normal user"

    def handle(self, *args, **options):

        # Username
        # -------------------------
        while True:
            username = input("Username: ").strip()

            if not username:
                self.stdout.write(
                    self.style.ERROR("Username cannot be empty.")
                )
                continue

            if User.objects.filter(username=username).exists():
                self.stdout.write(
                    self.style.ERROR(
                        f'Username "{username}" already exists.'
                    )
                )
                continue

            break

        # Email
        # -------------------------
        email_validator = EmailValidator()

        while True:
            email = input("Email: ").strip()

            if not email:
                self.stdout.write(
                    self.style.ERROR("Email cannot be empty.")
                )
                continue

            try:
                email_validator(email)
            except ValidationError:
                self.stdout.write(
                    self.style.ERROR("Please enter a valid email address.")
                )
                continue

            if User.objects.filter(email=email).exists():
                self.stdout.write(
                    self.style.ERROR(
                        f'Email "{email}" already exists.'
                    )
                )
                continue

            break
        
        # Mobile Number
        # -------------------------
        while True:
            mobile_number = input("Mobile number: ").strip()

            if not mobile_number:
                self.stdout.write(
                    self.style.ERROR("Mobile number cannot be empty.")
                )
                continue

            if UserProfile.objects.filter(
                mobile_number=mobile_number
            ).exists():
                self.stdout.write(
                    self.style.ERROR(
                        f'Mobile number "{mobile_number}" already exists.'
                    )
                )
                continue

            break
        
        # Password
        # -------------------------
        while True:

            password = getpass("Password: ")
            password2 = getpass("Password (again): ")

            if not password:
                self.stdout.write(
                    self.style.ERROR("Password cannot be empty.")
                )
                continue

            if password != password2:
                self.stdout.write(
                    self.style.ERROR("Passwords do not match.")
                )
                continue

            temp_user = User(
                username=username,
                email=email,
            )

            try:
                validate_password(password, user=temp_user)
            except ValidationError as error:

                for message in error.messages:
                    self.stdout.write(
                        self.style.ERROR(message)
                    )

                continue

            break

        # Create User
        # -------------------------
        with transaction.atomic():
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
            )
            
            user.userprofile.mobile_number = mobile_number
            user.userprofile.save()

            self.stdout.write("")
            self.stdout.write(
                self.style.SUCCESS(
                    f'User "{user.username}" created successfully.'
                )
            )