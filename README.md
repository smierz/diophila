# diophila
Python API Wrapper for [OpenAlex](http://openalex.org/).

### Entities / Endpoints
OpenAlex currently describes five different [scholarly entity types](https://docs.openalex.org/about-the-data) 
and their connections: 
* [Authors](https://docs.openalex.org/about-the-data/author)
* [Concepts](https://docs.openalex.org/about-the-data/concept)
* [Institutions](https://docs.openalex.org/about-the-data/institution)
* [Venues](https://docs.openalex.org/about-the-data/venue)
* [Works](https://docs.openalex.org/about-the-data/work)

Each entity type comes with an endpoint of the same name that can be queried
for a single (random or specific) entity or multiple (grouped or listed) entities.

### Installation
```commandline
pip (or pip3) install diophila
```

### Usage
First off, you need to initialize a client. The client offers all methods to query the API.

```Python
from diophila import OpenAlex

openalex = OpenAlex()
```

You can use the client to query for a [single random entity](https://docs.openalex.org/api/get-single-entities#random-entity) 
with the method `get_random_<entity>`:
```Python
random_author = openalex.get_random_author()
random_author['orcid']
```

Or if you have a [specific entity](https://docs.openalex.org/api/get-single-entities) in mind, you can use the client
using one of the entity's IDs via the `get_single_<entity>` method:
```Python
specific_work = openalex.get_single_work("https://doi.org/10.1364/PRJ.433188", "doi")
specific_work['display_name']
```

If you are interested in [entities grouped](https://docs.openalex.org/api/get-groups-of-entities) into facets, 
use the `get_groups_of_<entities>` method:
```Python
grouped_institutions = openalex.get_groups_of_institutions("type")
for group in grouped_institutions['group_by']:
    group['key']
```

And last but not least you can get [multiple entities](https://docs.openalex.org/api/get-lists-of-entities) from a type
in a list by using the `get_list_of_<entities>` method. Note that this method uses pagination,
either [basic paging](https://docs.openalex.org/api#basic-paging) or 
[cursor paging](https://docs.openalex.org/api#cursor-paging) 
depending on whether the `pages` parameter is supplied:
```Python
# if no `pages` parameter is supplied, we use cursor paging
pages = None
# if `pages` parameter is supplied, we use basic paging
pages = [1, 2, 3]

filters = {"is_oa": "true",
           "works_count": ">15000"}
pages_of_venues = openalex.get_list_of_venues(filters=filters, pages=pages)

for page in pages_of_venues:        # loop through pages
    for venue in page['results']:   # loop though list of venues
        venue['id']
```

### The Polite Pool
It's a good idea to use OpenAlex [polite pool](https://docs.openalex.org/api#the-polite-pool) 
which offers faster response times for users providing an email address.
If you would like to use it, simply initialize the client with your email address.

```Python
from diophila import OpenAlex

openalex = OpenAlex("your-email@address.com")
```

### Rate limits
The API currently doesn't have [rate limits](https://docs.openalex.org/api#rate-limits). 
However, if you need more than 100,000 calls per day,
please drop the OpenAlex team a line at team@ourresearch.org
or alternatively look into [using a snapshot](https://docs.openalex.org/download-snapshot).

### Citation
If you are using OpenAlex in your research, they kindly ask you to cite https://doi.org/10.48550/arXiv.2205.01833
