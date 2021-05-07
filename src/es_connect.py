from elasticsearch import Elasticsearch


def es_connect(info, start_day, qry):

    es_client = ""

    try:

        es_client = Elasticsearch([info['ANALYSIS_1'],
                                   info['ANALYSIS_2'],
                                   info['ANALYSIS_3']],
                                  port=info['PORT'],
                                  http_auth=(info['ID'], info['PWD']))

        es_data = es_client.search(index=info['INDEX_NAME'], body=qry.ES_DLS_01 % start_day)

        data = es_data['aggregations']['config']

        list_buckets = []

        if "buckets" in data:
            for buckets in data['buckets']:
                list_buckets.append(buckets)

        es_client.close()
        return list_buckets

    except Exception as err:
        print(err)
        es_client.close()


def m_es_connect(info, start_day, qry):

    es_client = ""

    try:

        es_client = Elasticsearch([info['ANALYSIS_1'],
                                   info['ANALYSIS_2'],
                                   info['ANALYSIS_3']],
                                  port=info['PORT'],
                                  http_auth=(info['ID'], info['PWD']))

        es_data = es_client.search(index=info['INDEX_NAME'], body=qry.ES_DLS_02 % start_day)

        data = es_data['aggregations']['target']

        list_buckets = []

        if "buckets" in data:
            for buckets in data['buckets']:
                list_buckets.append(buckets)

        es_client.close()
        return list_buckets

    except Exception as err:
        print(err)
        es_client.close()
