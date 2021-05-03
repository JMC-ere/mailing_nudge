import json
from src.es_connect import es_connect
from src.db_connect import db_connect

if __name__ == '__main__':
    with open("../config/info.json", 'r') as connect_info:
        info = json.load(connect_info)
    info = info['STG']

    es_connect(info)
    db_connect(info)

    connect_info.close()

