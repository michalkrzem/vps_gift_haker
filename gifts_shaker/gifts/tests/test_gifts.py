import json

import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

from login.forms import CreateUserForm


# --------------Test Login--------------
@pytest.mark.django_db
def test_home_correct_address(client):
    username = "username@gmail.com"
    password = "password12345"
    user_model = get_user_model()
    assert user_model.objects.count() == 0

    user_model.objects.create_user(
        username=username,
        password=password,
    )
    assert user_model.objects.count() == 1
    client.login(username=username, password=password)

    response = client.get(reverse("home"))

    assert response.status_code == 200


def test_home_incorrect_address(client):
    response = client.get(f'{reverse("home")}_incorrect')

    assert response.status_code == 404


# --------------Test Registration--------------
@pytest.mark.django_db
def test_all_gifts_correct_address(client):
    username = "username@gmail.com"
    password = "password12345"
    user_model = get_user_model()

    assert user_model.objects.count() == 0

    user_model.objects.create_user(
        username=username,
        password=password,
    )
    assert user_model.objects.count() == 1
    client.login(username=username, password=password)

    response = client.get(reverse("all_gifts"))

    assert response.status_code == 200


def test_all_gifts_incorrect_address(client):
    response = client.get(f'{reverse("all_gifts")}_incorreckt')

    assert response.status_code == 404
