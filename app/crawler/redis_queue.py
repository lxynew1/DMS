# To manager queues.
# author：black_liu
# date：2020-1-10

import redis
from .sql import Oracle


class Queue(object):
    def __init__(self):
        '''
        To build a connection pool.
        '''
        self.conn_pool = redis.ConnectionPool(host='10.73.9.21',
                                              port='6379',
                                              password='',
                                              decode_responses=True,
                                              db='1')

        self.re_pool = redis.Redis(connection_pool=self.conn_pool)

    def putIn(self, queue_type, value):
        '''
        Put a value into queues with queue type.
        :param queue_type:The value's type
        :param value:
        :return:None
        '''
        self.re_pool.rpush(queue_type, value)

    def getOut(self, queue_type):
        '''
        Take a value from queues with queue type.
        :param queue_type:The value's type
        :param value:
        :return:A value which taken from queues.
        '''
        value = self.re_pool.blpop(queue_type)[1]
        return value

    def queueCount(self, queue_type):
        '''
        The count of onequeue.
        :return:A value.
        '''
        count_value = self.re_pool.llen(queue_type)
        return count_value

if __name__=="__main__":
    q=Queue()
    o = Oracle()
    while True:
        r = o.getVillage2Queue()
        fid = r[0]
        village_name = r[1]
        o.updateVillageState(fid, 2)
        l = '{0}&&&{1}'.format(fid, village_name)
        q.putIn(queue_type="village", value=l)
    o.close()
