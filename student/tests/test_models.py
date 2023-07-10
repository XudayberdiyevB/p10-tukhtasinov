import pytest
from model_bakery import baker


@pytest.mark.django_db
def test_student_str():
    full_name = "Test student"
    student = baker.make("student.Student", full_name=full_name)
    assert str(student) == full_name
