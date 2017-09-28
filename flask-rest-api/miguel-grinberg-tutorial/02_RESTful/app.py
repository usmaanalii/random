from flask import Flask
from flask_restful import Api, Resource, reqparse, fields, marshal
from flask_httpauth import HTTPBasicAuth

auth = HTTPBasicAuth()
app = Flask(__name__)
api = Api(app)

task_fields = {
    'title': fields.String,
    'description': fields.String,
    'done': fields.Boolean,
    'uri': fields.Url('task')
}


class UserAPI(Resource):
    def get(self, id):
        pass

    def put(self, id):
        pass

    def delete(self, id):
        pass


class TaskListAPI(Resource):
    # decorators = [auth.login_required]

    def __init__(self):
        self.reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type=str, required=True, help='No task title provided', location='json')
        super(TaskListAPI, self).__init__()

    def get(self):
        pass

    def post(self):
        pass


class TaskAPI(Resource):
    # decorators = [auth.login_required]

    def __init__(self):
        self.reqparse.RequestParser()
        self.reqparse.add_argument(
            'title', type=str, required=True, location='json')
        self.reqparse.add_argument('description', type=str, location='json')
        self.reqparse.add_argument('done', type=bool, location='json')
        super(TaskAPI, self).__init__()

    def get(self, id):
        pass

    def put(self, id):
        task = filter(lambda t: t['id'] == id, tasks)
        if len(task) == 0:
            abort(404)
        task = task[0]
        args = self.reqparse.parse_args()
        for key, val in args.iteritems():
            if val is not None:
                task[key] = val
        return {'task': marshal(task, task_fields)}

    def delete(self, id):
        pass


api.add_resource(UserAPI, '/users/<int:id>', endpoint='user')
api.add_resource(TaskListAPI, '/todo/api/v1.0/tasks', endpoint='tasks')
api.add_resource(TaskAPI, '/todo/api/v1.0/tasks/<int:id>', endpoint='task')

if __name__ == '__main__':
    app.run(debug=True)
