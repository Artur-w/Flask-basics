from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort

app = Flask(__name__)
api = Api(app)

meme_put_args = reqparse.RequestParser()
meme_put_args.add_argument("name", type=str, help="Name of meme")
meme_put_args.add_argument("likes", type=int, help="likes of meme")

memes = {}

def abort_if_no_id(meme_id):
    if meme_id not in memes:
        abort(404, message="Meme ID do not exists")

def abort_if_meme(meme_id):
    if meme_id in memes:
        abort(409, message=f'Meme with {meme_id} already exists')
class Meme(Resource):
    def get(self, meme_id):
        abort_if_no_id(meme_id)
        return memes[meme_id]

    def put(self, meme_id):
        abort_if_meme(meme_id)
        args = meme_put_args.parse_args()
        memes[meme_id] = args
        return memes[meme_id], 201

    def delete(self, meme_id):
        abort_if_no_id(meme_id)
        del memes[meme_id]
        return '', 204

api.add_resource(Meme, '/meme/<int:meme_id>')

if __name__ == "__main__":
    app.run(debug=True)