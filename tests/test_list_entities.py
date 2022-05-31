import pytest
from diophila import OpenAlex

openalex = OpenAlex()


@pytest.mark.vcr
def test_list_of_entities_all_defaults():
    concept_pages = openalex.get_list_of_concepts()
    first_page = next(concept_pages)
    assert first_page['meta']['next_cursor'] is not None
    assert first_page['results'][0]['id'].startswith("https://openalex.org/C")


@pytest.mark.vcr
def test_list_of_entities_cursor_ends():
    filters = {"doi": "https://doi.org/10.1371/journal.pone.0266781|https://doi.org/10.1371/journal.pone.0267149"}
    work_pages = openalex.get_list_of_works(filters)
    first_page = next(work_pages)
    assert first_page['meta']['next_cursor'] is not None
    assert len(first_page['results']) == 2

    second_page = next(work_pages)
    assert second_page['meta']['next_cursor'] is None
    assert len(second_page['results']) == 0


@pytest.mark.vcr
def test_list_of_entities_basic_paging():
    pages = [1, 3]
    author_pages = openalex.get_list_of_authors(pages=pages)
    assert len(list(author_pages)) == len(pages)
    for page in author_pages:
        assert page['results'][0]['id'].startswith("https://openalex.org/A")
        assert page['meta']['page'] in pages


@pytest.mark.vcr
def test_list_of_entities_basic_paging_pages_exceeding():
    pages = [1, 401]
    author_pages = openalex.get_list_of_authors(pages=pages)
    assert len(list(author_pages)) == len(pages) - 1


@pytest.mark.vcr
def test_list_of_entities_per_page():
    per_page = 100
    venue_pages = openalex.get_list_of_venues(per_page=per_page)
    first_page = next(venue_pages)
    assert first_page['meta']['per_page'] == per_page


@pytest.mark.vcr
def test_list_of_entities_per_page_too_low():
    per_page = 0
    venue_pages = openalex.get_list_of_venues(per_page=per_page)
    first_page = next(venue_pages)
    assert first_page['meta']['per_page'] == 25


@pytest.mark.vcr
def test_list_of_entities_per_page_too_high():
    per_page = 201
    venue_pages = openalex.get_list_of_venues(per_page=per_page)
    first_page = next(venue_pages)
    assert first_page['meta']['per_page'] == 200


def test_list_of_entities_basic_paging_no_valid_pages():
    pages = [0, 401]
    author_pages = openalex.get_list_of_authors(pages=pages)
    assert len(list(author_pages)) == 0


# test for exceptions
def test_list_filter_is_not_filterable_attr():
    filters = {"hallo": "test"}
    with pytest.raises(ValueError):
        openalex.get_list_of_works(filters)


def test_list_sort_key_not_valid():
    sort = {"hallo": "asc"}
    with pytest.raises(ValueError):
        openalex.get_list_of_works(sort=sort)


def test_list_sort_value_not_valid():
    sort = {"display_name": "xyz"}
    with pytest.raises(ValueError):
        openalex.get_list_of_works(sort=sort)
