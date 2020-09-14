from flask import Flask, request
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
api = Api(app)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
db = SQLAlchemy(app)

class MemeModel(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(256), nullable=False)
    likes = db.Column(db.Integer, nullable=False)

    def __repr__(self):
        return f'Meme(name={name}, likes={likes})'

meme_put_args = reqparse.RequestParser()
meme_put_args.add_argument("name", type=str, help="Name of meme")
meme_put_args.add_argument("likes", type=int, help="likes of meme")

meme_update_args = reqparse.RequestParser()
meme_update_args.add_argument("name", type=str, help="Name of meme")
meme_update_args.add_argument('likes', type=int, help='Number of likes of meme')

resource_field = {
    'id': fields.Integer,
    'name': fields.String,
    'likes': fields.Integer
}

class Meme(Resource):
    @marshal_with(resource_field)
    def get(self, meme_id):
        result = MemeModel.query.filter_by(id=meme_id).first()
        if not result:
            abort(404, message='Could not find ID')
        return result

    @marshal_with(resource_field)
    def put(self, meme_id):
        args = meme_put_args.parse_args()
        result = MemeModel.query.filter_by(id=meme_id).first()
        if result:
            abort(409, message="ID taken!")
        meme = MemeModel(id=meme_id, name=args['name'], likes=args['likes'])
        db.session.add(meme)
        db.session.commit()
        return meme, 201

    def patch(self, meme_id):
        args = meme_update_args.parse_args()
        result = MemeModel.query.filter_by(id=meme_id).first()
        if not result:
            abort(404, message='Meme ID dont exist')
        if 'name' in args and args['name'] is not None:
            result.name = args['name']
        if args['likes']:
            result.likes = args['likes']
        db.session.commit()
        return result

    def delete(self, meme_id):
        meme = MemeModel.query.filter_by()
        if meme:
            db.session.delete(meme)
            db.session.commit()
        return f'Meme ID {meme_id} deleted', 204


api.add_resource(Meme, '/meme/<int:meme_id>')

if __name__ == "__main__":
    app.run(debug=True)