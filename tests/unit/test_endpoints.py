"""All unit tests covering class 'endpoints'."""

import pytest
from diophila.endpoints import Venues

endpoint = Venues(None)


# test method "build_filter_param"
def test_build_filter_param_empty_filters_should_give_none():
    filters = {}
    filter_param = endpoint._Endpoint__build_filter_param(filters=filters)
    assert filter_param is None


def test_build_filter_param_valid_filters_should_give_filter_string():
    filters = {"display_name.search": "test",
               "has_issn": "test",
               "publisher": "test"}
    filter_param = endpoint._Endpoint__build_filter_param(filters=filters)
    assert filter_param == "display_name.search:test,has_issn:test,publisher:test"


def test_build_filter_param_no_valid_filters_error():
    filters = {"hallo": "test"}
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_filter_param(filters=filters)


# test method "is_search"
def test_is_search_no_filter_no_search():
    filters = None
    search = None
    is_search = endpoint._Endpoint__is_search(filters=filters, search=search)
    assert is_search is False


def test_is_search_with_search():
    filters = {}
    search = "hallo"
    is_search = endpoint._Endpoint__is_search(filters=filters, search=search)
    assert is_search is True


def test_is_search_even_with_empty_search():
    filters = {}
    search = ""
    is_search = endpoint._Endpoint__is_search(filters=filters, search=search)
    assert is_search is True


def test_is_search_with_search_in_filters():
    filters = {"display_name.search": "hallo", "has_issn": "test"}
    search = None
    is_search = endpoint._Endpoint__is_search(filters=filters, search=search)
    assert is_search is True


def test_is_search_no_search_filter_no_search():
    filters = {"has_issn": "test"}
    search = None
    is_search = endpoint._Endpoint__is_search(filters=filters, search=search)
    assert is_search is False


# test method "build_group_by_param"
def test_build_group_by_param_empty_groupby_error():
    groupby = ""
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_group_by_param(groupby)


def test_build_group_by_param_no_valid_groupby_error():
    groupby = "hallo"
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_group_by_param(groupby)


def test_build_group_by_param_excluded_groupby_error():
    groupby = "doi"
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_group_by_param(groupby)


def test_build_group_by_param_valid_groupby_should_give_groupby_string():
    groupby = "has_issn"
    groupby_param = endpoint._Endpoint__build_group_by_param(groupby)
    assert groupby_param == groupby


# test method "build_sort_param_for_groups"
def test_build_sort_param_for_groups_empty_sort_should_give_none():
    sort = {}
    sort_param = endpoint._Endpoint__build_sort_param_for_groups(sort)
    assert sort_param is None


def test_build_sort_param_for_groups_all_valid_combos():
    sortable_keys = endpoint.sortable_attrs_for_groups
    sortable_values = endpoint.sortable_drctns
    for k in sortable_keys:
        for v in sortable_values:
            sort_param = endpoint._Endpoint__build_sort_param_for_groups({k: v})
            assert sort_param == f'{k}:{v}'


def test_build_sort_param_for_groups_multiple_values():
    sort = {"count": "asc", "key": "desc"}
    sort_param = endpoint._Endpoint__build_sort_param_for_groups(sort)
    assert sort_param == "count:asc,key:desc"


def test_build_sort_param_for_groups_no_valid_sort_error():
    sort = {"hallo": "test", "key": "desc"}
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_sort_param_for_groups(sort)


# test method "build_sort_param_for_list"
def test_build_sort_param_for_list_empty_sort_should_give_none():
    sort = {}
    sort_param = endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=False)
    assert sort_param is None


def test_build_sort_param_for_list_all_valid_combos():
    # relevance_score is handled separately
    sortable_keys = filter(lambda x: x != "relevance_score", endpoint.sortable_attrs)
    sortable_values = endpoint.sortable_drctns
    for k in sortable_keys:
        for v in sortable_values:
            sort = {k: v}
            is_search = False
            sort_param = endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=is_search)
            assert sort_param == f'{k}:{v}'


def test_build_sort_param_for_list_relevance_score_with_search():
    sort = {"relevance_score": "desc"}
    is_search = True
    sort_param = endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=is_search)
    assert sort_param == "relevance_score:desc"


def test_build_sort_param_for_list_relevance_score_asc_error():
    sort = {"relevance_score": "asc"}
    is_search = True
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=is_search)


def test_build_sort_param_for_list_relevance_score_without_search_error():
    sort = {"relevance_score": "desc"}
    is_search = False
    with pytest.raises(ValueError):
        assert endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=is_search)


def test_build_sort_param_for_list_multiple_values():
    sort = {"display_name": "asc", "works_count": "desc"}
    is_search = False
    sort_param = endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=is_search)
    assert sort_param == "display_name:asc,works_count:desc"


def test_build_sort_param_for_list_no_valid_sort_no_search_error():
    sort = {"hallo": "test", "key": "desc"}
    is_search = False
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=is_search)


def test_build_sort_param_for_list_no_valid_sort_search_error():
    sort = {"hallo": "test", "key": "desc"}
    is_search = True
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_sort_param_for_list(sort=sort, is_search=is_search)
