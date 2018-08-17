import pymysql


def get_connect(db):
    """连接mysql数据库"""
    connect = pymysql.connect(host="127.0.0.1", user="root",
                              passwd="zqzhang", db=db, charset="utf8")
    return connect
