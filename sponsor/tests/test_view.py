import pytest
from django.urls import reverse


@pytest.mark.django_db
class TestApplicationFormView:
    def test_create_application_form(self, client):
        url = reverse("sponsor-create")
        data = {
            "id": 1,
            "full_name": "xx xx",
            "phone": "+9987234354",
            "amount": 34,
            "is_organization": True,
            "status": "in_process",
            "created_at": "7.10.2023",
            "organization_name": "Book",
        }

        response = client.post(url, data=data)
        assert response.status_code == 201
