import uuid

from app.models import USER_CALENDAR
from . import crawler
from .sql import Oracle
from flask import request
from .redis_queue import Queue
import json

q=Queue()


@crawler.route('/get_village')
def getVillage():
    result = q.getOut(queue_type="village")
    r = result.split("&&&")
    fid = r[0]
    village_name = r[1]
    return_dict = {
        "fid":fid,
        "village_name":village_name
    }
    return json.dumps(return_dict, ensure_ascii=False)



@crawler.route('/putin_village')
def putInVillage():
    print("开始放入数据")
    o = Oracle()
    r = o.getVillage2Queue()
    fid = r[0]
    village_name = r[1]
    o.updateVillageState(fid, 2)
    o.close()
    l = '{0}&&&{1}'.format(fid,village_name)
    print("asd")
    q.putIn(queue_type="village",value=l)
    return '正在执行加入village'

@crawler.route('/update_village')
def updateVillage():
    pass