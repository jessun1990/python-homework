# coding: utf-8
# 第 0002 题：将 0001 题生成的 200 个激活码（或者优惠券）保存到 MySQL 关系型数据库中。
import pymysql

from .generater import generater


def generaterToMySql(add_num, code_length):
    db = pymysql.connect(
        host="localhost",
        db="py3homework",
        user="root",
        password="root",
    )

    cursor = db.cursor()
    cursor.execute("DROP TABLE IF EXISTS ACODES")
    sql_Creat = """ CREATE TABLE ACODES (
                    ID int NOT NULL AUTO_INCREMENT,
                    CODES varchar(200),
                    PRIMARY KEY (ID) )
                """
    cursor.execute(sql_Creat)
    for i in range(add_num):
        sql = " INSERT INTO ACODES(CODES) VALUES ('{0}') ".format(generater(random_length=code_length))
        cursor.execute(sql)
        db.commit()
    db.close()

if __name__ == '__main__':
    generaterToMySql(200, 20)
