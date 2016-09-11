from elasticsearch import Elasticsearch
from enum import Enum,unique
from django.conf import settings

class SearchIndex(Enum):
    blog  = 'blog'

class SearchType(Enum):
    entity = 'entity'


class SearchService(object):

    client = None

    @staticmethod
    def getClient():
        if SearchService.client:
            pass
        else:
            print(settings.ELASTICSEARCH)
            SearchService.client = Elasticsearch([settings.ELASTICSEARCH['host']+':'+settings.ELASTICSEARCH['port']])
        return SearchService.client
