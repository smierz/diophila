import pytest
from diophila import OpenAlex

openalex = OpenAlex()


# tests for /authors endpoint
@pytest.mark.vcr
def test_authors_group_by():
    group_by = "has_orcid"
    grouped_authors = openalex.get_groups_of_authors(group_by)
    assert len(grouped_authors['group_by']) == 2


@pytest.mark.vcr
def test_authors_group_by_with_filter():
    group_by = "has_orcid"
    filters = {"works_count": ">20000"}
    grouped_authors = openalex.get_groups_of_authors(group_by, filters)
    assert grouped_authors['group_by'][0]['count'] == 0


@pytest.mark.vcr
def test_authors_group_by_with_sort():
    group_by = "last_known_institution.type"
    sort = {"key": "asc"}
    grouped_authors = openalex.get_groups_of_authors(group_by, None, sort)
    assert grouped_authors['group_by'][0]['key'] == "archive"


# tests for /concepts endpoint
@pytest.mark.vcr
def test_concepts_group_by():
    group_by = "level"
    grouped_concepts = openalex.get_groups_of_concepts(group_by)
    assert len(grouped_concepts['group_by']) == 6


@pytest.mark.vcr
def test_concepts_group_by_with_filter():
    group_by = "level"
    filters = {"level": ">3"}
    grouped_concepts = openalex.get_groups_of_concepts(group_by, filters)
    assert grouped_concepts['group_by'][0]['key'] == '4'


@pytest.mark.vcr
def test_concepts_group_by_with_sort():
    group_by = "level"
    sort = {"key": "desc"}
    grouped_concepts = openalex.get_groups_of_concepts(group_by, None, sort)
    assert grouped_concepts['group_by'][0]['key'] == '5'


# tests for /institutions endpoint
@pytest.mark.vcr
def test_institutions_group_by():
    group_by = "has_ror"
    grouped_institutions = openalex.get_groups_of_institutions(group_by)
    assert len(grouped_institutions['group_by']) == 2


@pytest.mark.vcr
def test_institutions_group_by_with_filter():
    group_by = "has_ror"
    filters = {"has_ror": "true"}
    grouped_institutions = openalex.get_groups_of_institutions(group_by, filters)
    assert grouped_institutions['group_by'][1]['key'] == 'false'
    assert grouped_institutions['group_by'][1]['count'] == 0


@pytest.mark.vcr
def test_institutions_group_by_with_sort():
    group_by = "type"
    sort = {"key": "asc", "count": "desc"}
    grouped_institutions = openalex.get_groups_of_institutions(group_by, None, sort)
    assert grouped_institutions['group_by'][0]['key'] == 'company'


# tests for /venues endpoint
@pytest.mark.vcr
def test_venues_group_by():
    group_by = "is_oa"
    grouped_venues = openalex.get_groups_of_venues(group_by)
    assert len(grouped_venues['group_by']) == 3


@pytest.mark.vcr
def test_venues_group_by_with_filter():
    group_by = "is_oa"
    filters = {"is_oa": "true"}
    grouped_venues = openalex.get_groups_of_venues(group_by, filters)
    assert grouped_venues['group_by'][0]['key'] == 'true'
    assert grouped_venues['group_by'][0]['count'] > 0


@pytest.mark.vcr
def test_venues_group_by_with_sort():
    group_by = "publisher"
    sort = {"key": "asc", "count": "desc"}
    grouped_venues = openalex.get_groups_of_venues(group_by, None, sort)
    assert grouped_venues['group_by'][0]['key'] == 'unknown'


# tests for /works endpoint
@pytest.mark.vcr
def test_works_group_by():
    group_by = "has_doi"
    grouped_works = openalex.get_groups_of_works(group_by)
    assert len(grouped_works['group_by']) == 2


@pytest.mark.vcr
def test_works_group_by_with_filter():
    group_by = "has_doi"
    filters = {"has_doi": "true"}
    grouped_works = openalex.get_groups_of_works(group_by, filters)
    assert grouped_works['group_by'][1]['key'] == 'false'
    assert grouped_works['group_by'][1]['count'] == 0


@pytest.mark.vcr
def test_works_group_by_with_sort():
    group_by = "type"
    sort = {"key": "asc", "count": "desc"}
    grouped_works = openalex.get_groups_of_works(group_by, None, sort)
    assert grouped_works['group_by'][0]['key'] == 'journal-article'


# test for exceptions
def test_groups_group_by_is_empty():
    group_by = None
    with pytest.raises(ValueError):
        openalex.get_groups_of_works(group_by)


def test_groups_group_by_is_not_groupable_attr():
    group_by = "cited_by_count"
    with pytest.raises(ValueError):
        openalex.get_groups_of_works(group_by)


def test_groups_sort_key_not_valid():
    group_by = "type"
    sort = {"hallo": "asc"}
    with pytest.raises(ValueError):
        openalex.get_groups_of_works(group_by, None, sort)

def test_groups_filter_is_not_filterable_attr():
    group_by = "type"
    filters = {"hallo": "test"}
    with pytest.raises(ValueError):
        openalex.get_groups_of_works(group_by, filters)
