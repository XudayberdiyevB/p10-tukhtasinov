import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_users_str():
    username = "Testuser"
    user = baker.make("users.User", username=username)
    assert str(user) == username