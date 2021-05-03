import json
from query_dls import qry_dls

from elasticsearch import Elasticsearch


def es_connect(info):

    es_client = ""

    try:

        es_client = Elasticsearch([info['ANALYSIS_1'],
                                   info['ANALYSIS_2'],
                                   info['ANALYSIS_3']],
                                  port=info['PORT'],
                                  http_auth=(info['ID'], info['PWD']))

        es_data = es_client.search(index=info['INDEX_NAME'], body=qry_dls.ES_DLS_01)

        data = es_data['aggregations']['config']

        if "buckets" in data:
            for buckets in data['buckets']:
                print(buckets)

    except Exception as err:
        print(err)

