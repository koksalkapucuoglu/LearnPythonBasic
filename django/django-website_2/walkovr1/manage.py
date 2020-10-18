#!/usr/bin/env python
"""Django's command-line utility for administrative tasks."""
import os
import sys


def main():
    os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'walkovr1.settings')
    try:
        from django.core.management import execute_from_command_line
    except ImportError as exc:
        raise ImportError(
            "Couldn't import Django. Are you sure it's installed and "
            "available on your PYTHONPATH environment variable? Did you "
            "forget to activate a virtual environment?"
        ) from exc
    execute_from_command_line(sys.argv)


if __name__ == '__main__':
    main()

from user.models import UserUser

users = UserUser.objects.all()
ulist = list(users)
user0 = ulist[0].__dict__
user1 = ulist[1].__dict__
user2 = UserUser.objects.get(username = "walkovr2")

print(user2.__dict__["username"])


if user0["username"] == user1["username"] :
    print("eşit")
else:
    print("eşit değil")
