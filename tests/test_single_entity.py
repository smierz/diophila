import pytest
from diophila import OpenAlex

openalex = OpenAlex()


# tests for /authors endpoint
@pytest.mark.vcr
def test_single_author_by_openalex_id():
    openalex_id = "A1969205032"
    single_author = openalex.get_single_author(openalex_id)
    assert single_author['id'] == f"https://openalex.org/{openalex_id}"


@pytest.mark.vcr
def test_single_author_by_mag_id():
    mag_id = "1969205032"
    id_type = "mag"
    single_author = openalex.get_single_author(mag_id, id_type)
    assert single_author['ids'][id_type] == mag_id


@pytest.mark.vcr
def test_single_author_by_orcid_id():
    orcid_id = "0000-0003-1613-5981"
    id_type = "orcid"
    single_author = openalex.get_single_author(orcid_id, id_type)
    assert single_author['ids'][id_type].endswith(orcid_id)


@pytest.mark.vcr
def test_single_author_by_orcid_url():
    orcid_url = "https://orcid.org/0000-0003-1613-5981"
    id_type = "orcid"
    single_author = openalex.get_single_author(orcid_url)
    assert single_author['ids'][id_type] == orcid_url


# tests for /concepts endpoint
@pytest.mark.vcr
def test_single_concept_by_openalex_id():
    openalex_id = "C71924100"
    single_concept = openalex.get_single_concept(openalex_id)
    assert single_concept['id'] == f"https://openalex.org/{openalex_id}"


@pytest.mark.vcr
def test_single_concept_by_mag_id():
    mag_id = "2780831525"
    id_type = "mag"
    single_concept = openalex.get_single_concept(mag_id, id_type)
    assert single_concept['ids'][id_type] == mag_id


@pytest.mark.vcr
def test_single_concept_by_wikidata_id():
    wikidata_id = "Q11190"
    id_type = "wikidata"
    single_concept = openalex.get_single_concept(wikidata_id, id_type)
    assert single_concept['ids'][id_type].endswith(wikidata_id)


@pytest.mark.vcr
def test_single_concept_by_wikidata_url():
    wikidata_url = "https://www.wikidata.org/wiki/Q11190"
    id_type = "wikidata"
    single_concept = openalex.get_single_concept(wikidata_url)
    assert single_concept['ids'][id_type] == wikidata_url


# tests for /institutions endpoint
@pytest.mark.vcr
def test_single_institution_by_openalex_id():
    openalex_id = "I19820366"
    single_institution = openalex.get_single_institution(openalex_id)
    assert single_institution['id'] == f"https://openalex.org/{openalex_id}"


@pytest.mark.vcr
def test_single_institution_by_mag_id():
    mag_id = "19820366"
    id_type = "mag"
    single_institution = openalex.get_single_institution(mag_id, id_type)
    assert single_institution['ids'][id_type] == mag_id


@pytest.mark.vcr
def test_single_institution_by_ror_id():
    ror_id = "034t30j35"
    id_type = "ror"
    single_institution = openalex.get_single_institution(ror_id, id_type)
    assert single_institution['ids'][id_type].endswith(ror_id)


@pytest.mark.vcr
def test_single_institution_by_ror_url():
    ror_url = "https://ror.org/034t30j35"
    id_type = "ror"
    single_institution = openalex.get_single_institution(ror_url)
    assert single_institution['ids'][id_type] == ror_url


# tests for /venues endpoint
@pytest.mark.vcr
def test_single_venue_by_openalex_id():
    openalex_id = "V2751751161"
    single_venue = openalex.get_single_venue(openalex_id)
    assert single_venue['id'] == f"https://openalex.org/{openalex_id}"


@pytest.mark.vcr
def test_single_venue_by_mag_id():
    mag_id = "1983995261"
    id_type = "mag"
    single_venue = openalex.get_single_venue(mag_id, id_type)
    assert single_venue['ids'][id_type] == mag_id


@pytest.mark.vcr
def test_single_venue_by_issn_id():
    issn_id = "1431-5890"
    id_type = "issn"
    single_venue = openalex.get_single_venue(issn_id, id_type)
    assert issn_id in single_venue['ids'][id_type]


@pytest.mark.vcr
def test_single_venue_by_issn_l_id():
    issn_l_id = "0931-7597"
    id_type = "issn_l"
    single_venue = openalex.get_single_venue(issn_l_id, id_type)
    assert single_venue['ids'][id_type] == issn_l_id


# tests for /works endpoint
@pytest.mark.vcr
def test_single_work_by_openalex_id():
    openalex_id = "https://openalex.org/W2741809807"
    single_work = openalex.get_single_work(openalex_id)
    assert single_work['id'] == openalex_id


@pytest.mark.vcr
def test_single_work_by_mag_id():
    mag_id = "2741809807"
    id_type = "mag"
    single_work = openalex.get_single_work(mag_id, id_type)
    assert single_work['ids'][id_type] == mag_id


@pytest.mark.vcr
def test_single_work_by_doi():
    doi = "10.7717/peerj.4375"
    id_type = "doi"
    single_work = openalex.get_single_work(doi, id_type)
    assert single_work['ids'][id_type].endswith(doi)


@pytest.mark.vcr
def test_single_work_by_doi_url():
    doi_url = "https://doi.org/10.7717/peerj.4375"
    id_type = "doi"
    single_work = openalex.get_single_work(doi_url)
    assert single_work['ids'][id_type] == doi_url


@pytest.mark.vcr
def test_single_work_by_pmid():
    pmid = "29456894"
    id_type = "pmid"
    single_work = openalex.get_single_work(pmid, id_type)
    assert single_work['ids'][id_type].endswith(pmid)


@pytest.mark.vcr
def test_single_work_by_pmid_url():
    pmid = "https://pubmed.ncbi.nlm.nih.gov/29456894"
    id_type = "pmid"
    single_work = openalex.get_single_work(pmid, id_type)
    assert single_work['ids'][id_type] == pmid


# test for exceptions
def test_single_no_id_value():
    with pytest.raises(ValueError):
        openalex.get_single_work(None)


def test_single_id_type_is_no_id_attr():
    doi = "10.7717/peerj.4375"
    id_type = "wrongtype"
    with pytest.raises(ValueError):
        openalex.get_single_work(doi, id_type)


def test_single_no_id_type_and_id_value_not_url_or_openalex():
    doi = "xyz"
    with pytest.raises(ValueError):
        openalex.get_single_work(doi)
