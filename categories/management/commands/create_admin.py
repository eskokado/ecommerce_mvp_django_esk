from django.core.management import BaseCommand, CommandError

from django.contrib.auth.models import User


class Command(BaseCommand):
    help = 'Create admin user'

    def add_arguments(self, parser):
        ...
        parser.add_argument(
            '-u',
            '--username',
            type=str,
            help='Define a username',
        )
        parser.add_argument(
            '-e',
            '--email',
            type=str,
            help='Define a email',
        )
        parser.add_argument(
            '-p',
            '--password',
            type=str,
            help='Define a password',
        )

    def handle(self, *args, **kwargs):
        if kwargs['username']:
            username = kwargs['username']
        else:
            username = 'admin'
        if kwargs['email']:
            email = kwargs['email']
        else:
            email = 'admin@example.com'
        if kwargs['password']:
            password = kwargs['password']
        else:
            password = 'admin1234'

        user = User.objects.filter(username="admin")
        if user:
            raise CommandError(f"Username `{username}` already taken.")

        user = User.objects.filter(email="admin@example.com")
        if user:
           raise CommandError(f"Email `{email}` already taken.")

        User.objects.create_superuser(
            username=username,
            password=password,
            email=email
        )
        self.stdout.write(f"Admin `{username}` successfully created!")
