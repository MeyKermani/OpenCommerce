from django.core.management.base import BaseCommand
from django.contrib.auth.models import User
from apps.accounts.models import UserProfile
class Command(BaseCommand):
    help = "Create missing profiles for existing users"

    created_profiles_count = 0
    existing_profiles_count = 0

    def handle(self, *args, **options):
        created_profiles_count = 0
        existing_profiles_count = 0

        for user in User.objects.all():
            profile, created = UserProfile.objects.get_or_create(user=user)
            if created:
                created_profiles_count += 1
                self.stdout.write(
                    self.style.SUCCESS(
                        f"Profile created for user: {user.username}"
                    )
                )
            else:
                existing_profiles_count +=1
                self.stdout.write(
                    self.style.WARNING(
                        f"Profile already exists for user {user.username}"
                    )
                )

        self.stdout.write(self.style.MIGRATE_HEADING("----Summary----"))
        self.stdout.write(self.style.SUCCESS(f"Successfully created {created_profiles_count} objects!"))
        self.stdout.write(self.style.WARNING(f"Already existed: {existing_profiles_count}"))
