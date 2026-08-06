from django.core.management.base import BaseCommand
from django.core.exceptions import ValidationError
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password

from getpass import getpass

class Command(BaseCommand):
  help = "Create a new user"

  def add_arguments(self, parser):
    parser.add_argument(
      "--username",
      default=None,
      type=str,
      help="Username of the new user"
    )

    parser.add_argument(
      "--email",
      default=None,
      type=str,
      help="Email of the new user"
    )

    parser.add_argument(
      "--password",
      default=None,
      type=str,
      help="password of new user"
    )

    parser.add_argument(
      "--repeat_password",
      default=None,
      type=str,
      help="Repeat the password"
    )

  def handle(self, *args, **options):
    username = options["username"]
    email = options["email"]
    password = options["password"]
    repeat_password = options["repeat_password"]

  
    while not username or User.objects.filter(username = username).exists():
      if not username:
        self.stdout.write(self.style.ERROR("Username cannot be empty."))
      else:
        self.stdout.write(self.style.ERROR("Username already exists."))

      self.stdout.write("Username: ", ending="")
      username = input().strip()

    while not email:
      self.stdout.write(self.style.ERROR("Email cannot be empty."))
      self.stdout.write("Email: ", ending="")
      email = input().strip()
      
    while True:
      if not password:
        self.stdout.write(self.style.ERROR("Password cannot be empty"))
      elif repeat_password != password:
        self.stdout.write(
            self.style.ERROR("Repeated password doesn't match the password")
        )
      else:
        try:
            validate_password(password)
            break 
        except ValidationError as e:
            for error in e.messages:
                self.stdout.write(self.style.ERROR(error))

      self.stdout.write("Password: ", ending="")
      password = input().strip()
      self.stdout.write("Repeat Password: ", ending="")
      repeat_password = input().strip()

    user = User.objects.create_user(
      username=username,
      email=email,
      password=password
    )

    self.stdout.write(
      self.style.SUCCESS(f"User '{user.username}' created successfully")
    )