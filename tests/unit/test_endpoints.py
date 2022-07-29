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
            assert sort_param== f'{k}:{v}'


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
    sort_param = endpoint._Endpoint__build_sort_param_for_list(sort, None)
    assert sort_param is None


def test_build_sort_param_for_list_relevance_score_with_search():
    sort = {"relevance_score": "asc"}
    filters = {"display_name.search": "test"}
    sort_param = endpoint._Endpoint__build_sort_param_for_list(sort, filters)
    assert sort_param == "relevance_score:asc"


def test_build_sort_param_for_list_relevance_score_empty_filter_error():
    sort = {"relevance_score": "asc"}
    filters = None
    with pytest.raises(ValueError):
        assert endpoint._Endpoint__build_sort_param_for_list(sort, filters)


def test_build_sort_param_for_list_relevance_score_no_search_filter_error():
    sort = {"relevance_score": "asc"}
    filters = {"cited_by_count": ">0"}
    with pytest.raises(ValueError):
        assert endpoint._Endpoint__build_sort_param_for_list(sort, filters)


def test_build_sort_param_for_list_all_valid_combos():
    sortable_keys = endpoint.sortable_attrs
    sortable_values = endpoint.sortable_drctns
    for k in sortable_keys:
        for v in sortable_values:
            if k != "relevance_score":
                sort_param = endpoint._Endpoint__build_sort_param_for_list({k: v}, None)
                assert sort_param == f'{k}:{v}'


def test_build_sort_param_for_list_multiple_values():
    sort = {"display_name": "asc", "works_count": "desc"}
    sort_param = endpoint._Endpoint__build_sort_param_for_list(sort, None)
    assert sort_param == "display_name:asc,works_count:desc"


def test_build_sort_param_for_list_no_valid_sort_error():
    sort = {"hallo": "test", "key": "desc"}
    with pytest.raises(ValueError):
        endpoint._Endpoint__build_sort_param_for_list(sort, None)
