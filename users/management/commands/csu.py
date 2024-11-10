from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):
    """Класс для создания superuser"""

    def handle(self, *args, **options):
        user = User.objects.create(
            email="jonnyzver78@gmail.com",
            is_staff=True,
            is_superuser=True,
        )
        user.set_password("Vlada220913")
        user.save()

        # print(f"Создание superuser  прошло успешно: {user.email} пароль: Vlada220913")
