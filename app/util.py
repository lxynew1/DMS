# __author__:LXY
# explain: ���ߺ���
import ast

from app import db


# ��дprint
def log(*args, **kwargs):
    # ʹ��log����print
    print('log==>', *args, **kwargs)


# ���ݿ��ѯ���json��ʽ��
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
