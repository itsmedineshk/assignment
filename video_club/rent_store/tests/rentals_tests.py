import pytest
from django.urls import reverse
from utils import login_simple_user
from rent_store.models import Movie, Rental


@pytest.mark.django_db
def test_get_rentals(client):
    """Test if we can GET the rentals list."""
    login_simple_user(client)

    url = reverse('rentals')
    response = client.get(url)
    assert response.status_code == 200


@pytest.mark.django_db
def test_get_rentals_unauthenticated(client):
    """Test if we can GET the rentals list, without being authenticated."""
    url = reverse('rentals')
    response = client.get(url)
    assert response.status_code == 403


@pytest.mark.django_db
def test_create_rental(client):
    """Test if a simple user can rent a movie."""
    user = login_simple_user(client)

    url = reverse('rentals')
    a_movie = list(Movie.objects.all())[0].uuid
    data = {"movie": a_movie, "user": user}
    response = client.post(url, data)
    assert response.status_code == 201


@pytest.mark.django_db
def test_get_rental(client):
    """Test if a simple user can get a movie rental."""
    user = login_simple_user(client)

    url = reverse('rentals')
    a_movie = list(Movie.objects.all())[0].uuid
    data = {"movie": a_movie, "user": user}
    client.post(url, data)

    the_rental = list(Rental.objects.all())[0]
    url = reverse('rental', args=[the_rental.uuid])
    response = client.get(url)

    assert response.status_code == 200


@pytest.mark.django_db
def test_patch_rental(client):
    """Test if a simple user can return a movie when no money in his wallet."""
    user = login_simple_user(client)

    # create a rental
    url = reverse('rentals')
    a_movie = list(Movie.objects.all())[0].uuid
    data = {"movie": a_movie, "user": user}
    client.post(url, data)

    # return the movie
    the_rental = list(Rental.objects.all())[0]
    url = reverse('rental', args=[the_rental.uuid])
    response = client.patch(url)

    assert response.status_code == 400


@pytest.mark.django_db
def test_patch_rental(client):
    """Test if a simple user can return a movie when enough money in his wallet."""
    user = login_simple_user(client)

    # create a rental
    url = reverse('rentals')
    a_movie = list(Movie.objects.all())[0].uuid
    data = {"movie": a_movie, "user": user}
    client.post(url, data)

    # add money to wallet
    url = reverse('profile')
    client.patch(url, data={"deposit": 10}, content_type='application/json')

    # return the movie
    the_rental = list(Rental.objects.all())[0]
    url = reverse('rental', args=[the_rental.uuid])
    response = client.patch(url, content_type='application/json')
    assert response.status_code == 200

    # assert that if user tries to return again the returned movie he gets 400
    response = client.patch(url, content_type='application/json')
    assert response.status_code == 400
