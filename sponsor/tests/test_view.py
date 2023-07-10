import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestApplicationFormView:
    def test_create_application_form_true(self, client):
        url = reverse("sponsor-create")
        data = {
            "id": 1,
            "full_name": "xx xx",
            "phone": "+9987234354",
            "amount": 34,
            "is_organization": True,
            "organization_name": "Book",
        }

        response = client.post(url, data=data)
        assert response.status_code == 201

    def test_create_application_form_false(self, client):
        url = reverse("sponsor-create")
        data = {
            "id": 1,
            "full_name": "xx xx",
            "phone": "+9987234354",
            "amount": 34,
            "is_organization": False,
            "organization_name": "Book",
        }

        response = client.post(url, data=data)
        assert response.status_code == 201
