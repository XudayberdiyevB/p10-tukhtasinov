import pytest
from django.test import TestCase
from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient

from sponsors.models import Sponsor
from sponsors.serializers import SponsorCreateSerializer


@pytest.mark.django_db
class TestApplicationFormView:
    def test_create_application_form_true(self, client):
        url = reverse("sponsors-create")
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
        url = reverse("sponsors-create")
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

    def test_sponsor_money_dashboard(self, client):
        url = reverse("sponsors-dashboard")
        response = client.get(url)
        assert response.status_code == 200


class SponsorListCreateViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("sponsor_list_create")
        self.sponsor_data = {
            "full_name": "Test Sponsor",
            "phone": "1234567890",
            "amount": 100,
            "is_organization": True,
            "organization_name": "Test Organization",
        }
        self.serializer = SponsorCreateSerializer(data=self.sponsor_data)

    def test_create_sponsor(self):
        response = self.client.post(self.url, self.sponsor_data)
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sponsor.objects.count(), 1)

    def test_create_sponsor_invalid_data(self):
        invalid_data = {"full_name": "Test Sponsor"}  # Missing required 'phone' field
        response = self.client.post(self.url, invalid_data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
        self.assertEqual(Sponsor.objects.count(), 0)

    def test_list_sponsors(self):
        Sponsor.objects.create(full_name="Sponsor 1", phone="1111111111", amount=200)
        Sponsor.objects.create(full_name="Sponsor 2", phone="2222222222", amount=300)

        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 5)


class SponsorDetailViewTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.sponsor = Sponsor.objects.create(
            full_name="Test Sponsor",
            phone="1234567890",
            amount=100,
            is_organization=True,
            organization_name="Test Organization",
        )
        self.url = reverse("sponsor_detail", kwargs={"pk": self.sponsor.pk})
        # self.serializer = SponsorDetailSerializer(instance=self.sponsor)  # noqa

    def test_retrieve_sponsor(self):
        response = self.client.get(self.url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, self.serializer.data)


class SponsorMoneyDashboardTest(TestCase):
    def setUp(self):
        self.client = APIClient()
        self.url = reverse("sponsor-dashboard")

    def test_get_sponsor_money_dashboard(self):
        self.client.get(self.url)
