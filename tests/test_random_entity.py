import pytest
from diophila import OpenAlex

openalex = OpenAlex()


@pytest.mark.vcr
def test_random_author():
    random_author = openalex.get_random_author()
    assert random_author['id'].startswith("https://openalex.org/A")


@pytest.mark.vcr
def test_random_concept():
    random_concept = openalex.get_random_concept()
    assert random_concept['id'].startswith("https://openalex.org/C")


@pytest.mark.vcr
def test_random_institution():
    random_institution = openalex.get_random_institution()
    assert random_institution['id'].startswith("https://openalex.org/I")


@pytest.mark.vcr
def test_random_venue():
    random_venue = openalex.get_random_venue()
    assert random_venue['id'].startswith("https://openalex.org/V")


@pytest.mark.vcr
def test_random_work():
    random_work = openalex.get_random_work()
    assert random_work['id'].startswith("https://openalex.org/W")
