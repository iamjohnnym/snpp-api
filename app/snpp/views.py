from app import api
from app.testdict import memory_data
from app.tasks import pager
from flask import jsonify, abort, request, make_response, url_for
from flask.views import MethodView
from flask.ext.restful import Resource, reqparse, fields, marshal
#from flask.ext.httpauth import HTTPBasicAuth

snpp_fields = {
        'type': fields.String,
        'destination': fields.String,
        'port': fields.String,
        'username': fields.String,
        'password': fields.String,
        'recipientList': fields.List(fields.String),
        'message': fields.String,
        'status': fields.String
        }

class SnppAPI(Resource):
    def __init__(self):
        self.reqparse = reqparse.RequestParser()
        self.reqparse.add_argument('type', type=str, required=True, help="no type provided", location='json')
        self.reqparse.add_argument('destination', type=str, required=True, help="no destination provided", location='json')
        self.reqparse.add_argument('port', type=str, required=True, help="no port provided", location='json')
        self.reqparse.add_argument('username', type=str, required=True, help="no username provided", location='json')
        self.reqparse.add_argument('password', type=str, required=True, help="no password provided", location='json')
        self.reqparse.add_argument('recipientList', type=list, required=True, help="no recipient provided", location='json')
        self.reqparse.add_argument('message', type=str, required=True, help="no message provided", location='json')
        super(SnppAPI, self).__init__()

    def get(self):
        return { 'snpp': map(lambda n: marshal(n, snpp_fields), memory_data) }

    def post(self):
        from snpplib import SNPP
        args = self.reqparse.parse_args()
        id = memory_data[-1]['id'] + 1
        snpp_req = {
                'id': id,
                'type': args['type'],
                'destination': args['destination'],
                'port': args['port'],
                'username': args['username'],
                'password': args['password'],
                'recipientList': args['recipientList'],
                'message': args['message'],
                'status': 'queued'
                }
        memory_data.append(snpp_req)
        msg = SNPP(
                debuglevel=0,
                host=args['destination'],
                port=int(args['port'])
                )
        msg.close()
        print pager.name
        status = pager.delay(id, msg, memory_data[id-1])
        print status.ready()
        print memory_data[id-1]['status']
        return {'event': marshal(snpp_req, snpp_fields) }, 201


api.add_resource(SnppAPI, '/api/snpp', endpoint='snpp')
