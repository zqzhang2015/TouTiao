import pymysql


def get_connect(db):
    """连接mysql数据库"""
    connect = pymysql.connect(host="zzqdb.clycmysqmdhd.us-east-2.rds.amazonaws.com", user="root",
                              passwd="zzq123456", db=db, charset="utf8")
    return connect
