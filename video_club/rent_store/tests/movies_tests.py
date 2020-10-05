import pytest
from django.urls import reverse
from utils import login_simple_user, login_superuser


@pytest.mark.django_db
def test_get_movies(client):
    """Test if we can GET the movie list."""
    login_simple_user(client)

    url = reverse('movies')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_movies_unauthenticated(client):
    """Test if we can GET the movie list, without being authenticated."""
    url = reverse('movies')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_get_movie(client):
    """Test if we can GET a specific movie."""
    login_simple_user(client)

    url = reverse('movies')
    response = client.get(url)
    first_uuid = response.data['results'][0]['uuid']
    url = reverse('movie', args=[first_uuid])
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_create_movie_simple_user(client):
    """Test if a simple user can create a movie."""
    login_simple_user(client)

    url = reverse('movies')
    data = {"name": "MyMovie", "pub_date": 2000, "duration": 100, "rating": 8.8, "description": "",
            "categories": "Action"}
    response = client.post(url, data)
    assert response.status_code == 403


@pytest.mark.django_db
def test_create_movie_superuser(client):
    """Test if a super-user can create a movie."""
    login_superuser(client)

    url = reverse('movies')
    data = {"name": "MyMovie", "pub_date": 2000, "duration": 100, "rating": 8.8, "description": "",
            "categories": "Action"}
    response = client.post(url, data)
    assert response.status_code == 201
