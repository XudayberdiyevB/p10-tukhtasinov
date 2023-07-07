import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_sponsor_str():
    full_name = "Test sponsor"
    sponsor = baker.make("sponsor.Sponsor", full_name=full_name)
    assert str(sponsor) == full_name
