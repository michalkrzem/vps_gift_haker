import json

import pytest
from django.test import Client
from django.contrib.auth.models import User
from django.contrib.auth import get_user_model
from django.urls import reverse

from login.forms import CreateUserForm


# --------------Test Login--------------
def test_login_correct_address(client):
    response = client.get(reverse("login"))

    assert response.status_code == 200


def test_login_incorrect_address(client):
    response = client.get(f'{reverse("login")}_incorrect')

    assert response.status_code == 404


@pytest.mark.parametrize(
    "username, password, expected",
    [
        ("username@gmail.com", "zaqwsxcde123", True),
        ("user_incorrect@gmail.com", "zaqwsxcde123", False),
        ("user_incorrect@gmail.com", "zaqw_incorrect", False),
        ("username@gmail.com", "zaqw_incorrect", False),
        ("user_incorrect@gmail.com", "zaqw_incorrect", False),
        ("username@gmail.com", "", False),
        ("username@gmail.com", "long_but_wuithout_numbers", False),
        ("", "", False),
    ],
)
@pytest.mark.django_db
def test_login_user_post_data(client, username, password, expected):
    user_model = get_user_model()
    assert user_model.objects.count() == 0

    user_model.objects.create_user(
        username="username@gmail.com",
        password="zaqwsxcde123",
    )
    assert user_model.objects.count() == 1
    assert client.login(username=username, password=password) == expected


# --------------Test Registration--------------
def test_register_correct_address(client):
    response = client.get(reverse("register"))

    assert response.status_code == 200


def test_register_incorrect_address(client):
    response = client.get(f'{reverse("register")}_incorreckt')

    assert response.status_code == 404


@pytest.mark.django_db
def test_register_user_client_post(client):
    response = client.post(
        path=reverse("register"),
        data={
            "username": "username@gmail.com",
            "first_name": "first_name",
            "last_name": "last_name",
            "password1": "password",
            "password2": "password",
        },
    )
    assert response.status_code == 200


@pytest.mark.django_db
def test_register_user_client_get(client):
    response = client.post(
        path="/login/register/",
    )
    assert response.status_code == 200


@pytest.mark.parametrize(
    "username, first_name, last_name, password1, password2, expected",
    [
        (
            "username@gmail.com",
            "Michal",
            "Krzem",
            "pasword12345",
            "pasword12345",
            True,
        ),
        (
            "user_incorrectgmail.com",
            "Michal",
            "Krzem",
            "pasword12345",
            "pasword12345",
            False,
        ),
        (
            "user_incorrect@gmail.com",
            "Michal",
            "Krzem",
            "zaqw_incorrect",
            "zaqw_incorr",
            False,
        ),
        ("username@gmail.com", "Michal", "Krzem", "to_sh", "to_sh", False),
        ("", "", "", "", "", False),
    ],
)
@pytest.mark.django_db
def test_register_user_client_post(
    client, username, first_name, last_name, password1, password2, expected
):
    user_model = get_user_model()
    assert user_model.objects.count() == 0

    response = client.post(
        path=reverse("register"),
        data={
            "username": username,
            "first_name": first_name,
            "last_name": last_name,
            "password1": password1,
            "password2": password2,
        },
        follow=True,
    )

    assert User.objects.filter(username=username).exists() == expected


@pytest.mark.django_db
def test_register_user_client_redirect(client):
    user_model = get_user_model()
    assert user_model.objects.count() == 0

    response = client.post(
        path=reverse("register"),
        data={
            "username": "username@gmail.com",
            "first_name": "Michał",
            "last_name": "Krzem",
            "password1": "pasword12345",
            "password2": "pasword12345",
        },
        follow=True,
    )
    assert user_model.objects.count() == 1
    assert response.redirect_chain[-1] == ("/login/login/", 302)


# --------------Test Logout--------------
@pytest.mark.django_db
def test_logout_user_client_redirect(client):
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

    response = client.post(
        path=reverse("logout"),
        follow=True,
    )

    assert response.redirect_chain[-1] == ("/login/login/", 302)
