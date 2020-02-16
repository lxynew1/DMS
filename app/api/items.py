from flask_restful import Resource


class HelloWorld(Resource):
    def post(self):
        return {'hello': 'post'}

    def get(self):
        return {'hello': 'get'}
