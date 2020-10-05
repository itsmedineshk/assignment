import pytest
from django.urls import reverse
from utils import login_simple_user


@pytest.mark.django_db
def test_get_categories(client):
    """Test if we can GET the category list."""
    login_simple_user(client)

    url = reverse('categories')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_categories_unauthenticated(client):
    """Test if we can GET the category list, without being authenticated."""
    url = reverse('categories')
    response = client.get(url)
    assert response.status_code == 403
