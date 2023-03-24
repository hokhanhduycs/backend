from flask import Flask, jsonify, request, redirect, url_for
from flask_restful import Resource, Api
from sqlalchemy import create_engine

app = Flask(__name__)
api = Api(app)

db_connect = create_engine('sqlite:///chinook.db')
db_connect = create_engine('sqlite:///chinook.db')
conn = db_connect.connect()

class Employees(Resource):
    def get(self):
        query = conn.execute("select * from employees") # Dòng này thực hiện truy vấn và trả về json
        return {'employees': [i[0] for i in query.cursor.fetchall()]}

class Hello(Resource):

    def get(self):
        return jsonify({'message': 'hello world'})
    def post(self):
        data = request.get_json()     # status code
        return jsonify({'data': data}), 201
    
api.add_resource(Employees, '/employees') # Route_1
api.add_resource(Hello, '/')

if __name__ == '__main':
    app.run(debug=True)