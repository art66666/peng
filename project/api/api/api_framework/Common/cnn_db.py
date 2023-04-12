import pymysql
class Db_util():
    def __init__(self):
        self.mydb = pymysql.connect(host = '192.168.6.96',
                             user = 'root',
                             password = 'root',
                             database = 'ioms-scada',
                             port = 3306)
        self.cursor = self.mydb.cursor(cursor=pymysql.cursors.DictCursor)
 
    def __del__(self):
        self.mydb.close()
        self.cursor.close()


    def selecttest(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data
 
    def update(self,sql):
        try:
            self.cursor.execute(sql)
            self.mydb.commit()
        except Exception as e:
            self.mydb.rollback()
            print('在更新数据库时发生错误了：{0}'.format(e))
 
    def insert(self,sql):
        try:
            self.cursor.execute(sql)
            self.mydb.commit()
        except Exception as e :
            self.mydb.rollback()
            print('在插入数据时发生错误了：{0}'.format(e))
 
 
if __name__ == '__main__':
    db = Db_util()
    print(db.selecttest("select * from i_point_info where point_name = '3'"))
