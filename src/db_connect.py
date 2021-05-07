import pymysql


def db_connect(info, qry):
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
        sql = qry.NUDGE_TYPE
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()

        list_data = []

        for i in rows:
            dict_data = {i['nudge_type']: i['nudge_name']}
            list_data.append(dict_data)

        conn.close()
        return list_data

    except Exception as err:
        print(err)
        conn.close()


def m_db_connect(info, qry):
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
        sql = qry.MENU_ID
        curs.execute(sql)

        # 데이타 Fetch
        rows = curs.fetchall()

        m_list_data = []

        for i in rows:
            dict_data = {i['menu_id']: i['exposure_name']}
            m_list_data.append(dict_data)

        conn.close()
        return m_list_data

    except Exception as err:
        print(err)
        conn.close()



