
import os
import pytest
import sys
from unittest.mock import patch
from faker import Faker
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), "../..")))
from algo_lib.simulation.simulate_people import generate_person, generate_people  # type: ignore


@pytest.fixture
def fake():
    """Fixture to provide a Faker instance."""
    return Faker("en_US")


@pytest.fixture
def temp_data_dir(tmp_path):
    """Fixture to provide a temporary data directory."""
    return tmp_path


def test_generate_person(fake, temp_data_dir):
    """Test the generate_person function."""
    person = generate_person(fake, data_dir=str(temp_data_dir))
    person_dir = temp_data_dir / person

    # Assert the directory was created
    assert person_dir.is_dir()

    # Assert the directory contains .gitkeep
    assert (person_dir / ".gitkeep").exists()

    # Assert the .gitkeep file content
    with open(person_dir / ".gitkeep", "r", encoding="utf8") as f:
        content = f.read()
    assert content == ""


def test_generate_people(fake, temp_data_dir):
    """Test the generate_people function."""
    num_people = 3
    generate_people(
        locale="en_US",
        num_people=num_people,
        data_dir=str(temp_data_dir)
        )

    # Assert the correct number of directories were created
    person_dirs = [d for d in temp_data_dir.iterdir() if d.is_dir()]
    assert len(person_dirs) == num_people

    # Assert each directory contains .gitkeep
    for person_dir in person_dirs:
        assert (person_dir / ".gitkeep").exists()


def test_generate_people_with_different_locale(temp_data_dir):
    """Test generate_people with a different locale."""
    num_people = 2
    generate_people(
        locale="it_IT",
        num_people=num_people,
        data_dir=str(temp_data_dir)
        )

    # Assert the correct number of directories were created
    person_dirs = [d for d in temp_data_dir.iterdir() if d.is_dir()]
    assert len(person_dirs) == num_people


def test_generate_people_empty_data_dir(temp_data_dir):
    """Test that generate_people creates directories in an empty data directory."""
    generate_people(locale="en_US", num_people=1, data_dir=str(temp_data_dir))

    # Assert the directory now contains one person's folder
    person_dirs = [d for d in temp_data_dir.iterdir() if d.is_dir()]
    assert len(person_dirs) == 1


def test_generate_person_empty_folder(fake, temp_data_dir):
    """Test generate_person handles existing empty folder."""
    mock_name = "tony_gonzalez"
    person_dir = temp_data_dir / mock_name

    # person_name = fake.name().replace(" ", "_").lower()
    # person_dir = temp_data_dir / person_name

    # Create the directory beforehand
    person_dir.mkdir(parents=True)

    # person = generate_person(fake, data_dir=str(temp_data_dir))
    with patch.object(fake, "name", return_value="Tony Gonzalez"):
        person = generate_person(fake, data_dir=str(temp_data_dir))

    # assert person == person_name
    assert person == mock_name

    # Assert the directory now contains .gitkeep
    assert (person_dir / ".gitkeep").exists()
