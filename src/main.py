import json
from make_xl import make_xl, m_make_xl
import sys
from datetime import datetime, timedelta
from query_dls import qry_dls
from db_connect import m_db_connect


if __name__ == '__main__':
    with open("../config/info.json", 'r') as connect_info:
        info = json.load(connect_info)
    info = info['STG']

    start_day = ['2021.05.05']

    # start_day = datetime.today().strftime("%Y.%m.%d")

    loop = 0

    qry = qry_dls

    for day in start_day:
        make_xl(info, day, qry)
        m_make_xl(info, day, qry)

    # if len(sys.argv) > 1:
    #     start_day = sys.argv[1]
    #     start_day = datetime.strptime(start_day, "%Y.%d.%m").date()
    #     start_day = start_day.strftime("%Y.%m.%d")
    #     make_xl(info, start_day, qry)
    #
    # if len(sys.argv) > 2:
    #     loop = int(sys.argv[2])
    #
    # if loop > 2:
    #     for i in range(0, loop):
    #         start_day = start_day + timedelta(days=loop)
    #         make_xl(info, start_day, qry)

    connect_info.close()

