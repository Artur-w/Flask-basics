from flask import Flask, request
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

memes = {}

class Meme(Resource):
    def get(self, meme_id):
        return memes[meme_id]

    def put(self, meme_id):
        print(request.form['likes'])
        return {}

api.add_resource(Meme, '/meme/<int:meme_id>')

if __name__ == "__main__":
    app.run(debug=True)