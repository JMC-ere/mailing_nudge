import pymysql
from query_dls import qry_dls


def db_connect(info):

    conn = ""

    try:
        # MySQL Connection 연결
        conn = pymysql.connect(host=info['DB_HOST'],
                               user=info['DB_USER'],
                               password=info['DB_PWD'],
                               db=info['DB_NAME'],
                               charset='utf8', cursorclass=pymysql.cursors.DictCursor)

        # Connection 으로부터 Cursor 생성
        curs = conn.cursor()

        # SQL문 실행
        sql = qry_dls.NUDGE_TYPE
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()

        print(rows)

    except Exception as err:
        print(err)


