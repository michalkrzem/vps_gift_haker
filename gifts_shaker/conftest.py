import pytest

from django.test import Client


@pytest.fixture
def client():
    client = Client(enforce_csrf_checks=True)

    return client
