import cx_Oracle


class Oracle(object):
    def __init__(self):
        self.connect = cx_Oracle.connect('SPIDER315/yunwei159@10.73.9.21:1521/bdc')
        self.cursor = self.connect.cursor()

    def getVillage2Queue(self):

        self.cursor.execute('''
        SELECT T.VILLAGE_NAME,T.FID FROM VILLAGE_LIST T WHERE T.STATE = 0
        ''')
        result = self.cursor.fetchone()
        fid, village_name = result[1], result[0]
        return fid,village_name

    def updateVillageState(self,fid,state):
        update_sql = '''UPDATE VILLAGE_LIST T SET T.STATE = {0} WHERE T.FID = '{1}' '''.format(state,fid)
        print(update_sql)
        self.cursor.execute(update_sql)
        self.connect.commit()

    def close(self):
        self.connect.close()

if __name__ == '__main__':
    o=Oracle()
    fid = o.getVillage2Queue()[0]
    o.updateVillageState(fid,1)
