# __author__:LXY
# explain: 工具函数
import ast

from app import db


# 重写print
def log(*args, **kwargs):
    # 使用log代替print
    print('log==>', *args, **kwargs)


# 数据库查询结果json格式化
def comments(Comment, UID):
    comments = db.session.query(Comment).filter_by(UID=UID).all()
    result = []
    for comment in comments:
        comment = "{ 'title':'" + comment.to_json()['TITLE'] + "','start' : '" + comment.to_json()[
            'START'] + "','end' : '" + comment.to_json()['END'] + "','url' : '" + comment.to_json()[
                      'URL'] + "','id':'" + comment.to_json()['id'] + "'}"
        comment = ast.literal_eval(comment)
        result.append(comment)
    # return jsonify(result)
    return result
