#!/usr/bin/env python

from flask import Flask
from flask_restful import Api

app = Flask(__name__)
api = Api(app)

from resources.todo import TodoListResource
from resources.todo import TodoResource
from resources.user import UserListResource
from resources.user import UserResource

api.add_resource(UserResource, '/login', endpoint='login')
api.add_resource(UserResource, '/users/<string:id>', endpoint='user')
api.add_resource(UserListResource, '/users', endpoint='users')
api.add_resource(TodoListResource, '/todos', endpoint='todos')
api.add_resource(TodoResource, '/todos/<string:id>', endpoint='todo')

if __name__ == '__main__':
    app.run(host="0.0.0.0",debug=True)
