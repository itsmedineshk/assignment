import pytest
from rent_store.models import CustomUser


@pytest.mark.django_db
def login_simple_user(client):
    user = CustomUser.objects.create_user(username="tempuser", password="tempuser")
    client.login(username="tempuser", password="tempuser")
    return user


@pytest.mark.django_db
def login_superuser(client):
    user = CustomUser.objects.create_user(username="tempuser", password="tempuser", is_superuser=True, is_staff=True)
    client.login(username="tempuser", password="tempuser")
    return user
