import pymysql


def get_stu_info():
    # 打开文件
    f = open('D://PyCharm/info_management_django/info_management_django/data/config.txt', 'r')
    # \n换行符需要删掉
    username = f.readline()[:-1]
    password = f.readline()[:-1]
    database_name = f.readline()[:-1]
    # 打开数据库连接 数据从配置文件中来 配置文件会被ignore掉
    db = pymysql.connect("localhost", username, password, database_name)
    # 关闭文件连接
    f.close()
    # 使用cursor()方法获取操作游标
    cursor = db.cursor()
    # SQL查询语句
    sql = "SELECT * FROM stu_info"
    try:
        # 执行sql语句
        cursor.execute(sql)
        # 执行sql语句
        db.commit()
        # 获取所有查询结果
        result = cursor.fetchall()
        # 表示执行成功
        print("执行成功")
    except:
        # 发生错误时回滚
        db.rollback()
        # 表示执行失败
        print("执行失败")
    # 关闭数据库连接
    db.close()
    return result
