import pytest
from django.urls import reverse
from utils import login_simple_user
from rent_store.models import CustomUser


@pytest.mark.django_db
def test_get_profile(client):
    """Test if a simple user can get his profile."""
    login_simple_user(client)

    url = reverse('profile')
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_deposit(client):
    """Test if a simple user can add money to his wallet."""
    user = login_simple_user(client)
    assert user.wallet == 0

    # add money to wallet
    url = reverse('profile')
    response = client.patch(url, data={"deposit": 10}, content_type='application/json')
    assert response.status_code == 200

    user = CustomUser.objects.get(id=user.id)
    assert user.wallet == 10
