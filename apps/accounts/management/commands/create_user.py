from django.core.management.base import BaseCommand, CommandError
from django.contrib.auth.models import User
from apps.accounts.models import UserProfile


class Command(BaseCommand):
    help = "Create a normal user with a profile.  the order of arguments : username, email, password"

    def add_arguments(self, parser):
        parser.add_argument(
            "username",
            type=str,
            help="Username for the user"
        )

        parser.add_argument(
            "email",
            type=str,
            help="Email address"
        )

        parser.add_argument(
            "password",
            type=str,
            help="Password"
        )

    def handle(self, *args, **options):

        try:
            username = options["username"]
            email = options["email"]
            password = options["password"]

            first_name = input("Enter first name (optional): ").strip()
            last_name = input("Enter last name (optional): ").strip()


            if User.objects.filter(username=username).exists():
                raise CommandError(
                    f"User '{username}' already exists"
                )

            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                first_name=first_name,
                last_name=last_name
            )

            add_mobile = input(
                "Do you want to add a mobile number? (y/n): "
            )


            if add_mobile.lower() == "y":
                mobile_number = input(
                    "Enter mobile number: "
                )
                profile = user.userprofile
                profile.mobile_number = mobile_number
                profile.save()


            self.stdout.write(
                self.style.SUCCESS(
                    f"Successfully created user: {username}"
                )
            )

        except Exception as e:
            raise CommandError(
                f"Failed to create user: {e}"
            )