from flask import Flask
from flask_restful import Api, Resource, reqparse, abort, fields, marshal_with
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)
app.config['SECRET_KEY'] = '5791628bb0b13ce0c676dfde280ba245'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'

db = SQLAlchemy(app)

api = Api(app)


class VideoModel(db.Model):
	id = db.Column(db.Integer, primary_key=True)
	name = db.Column(db.String(100), nullable=False)
	views = db.Column(db.Integer, nullable=False)
	likes = db.Column(db.Integer, nullable=False)

	def __repr__(self):
		return f"Video(name = {self.name}, views = {self.views}, likes = {self.likes})"


# response = requests.put(base + "video/1", data_new)
# set de record data_new={}
video_put_args = reqparse.RequestParser()
video_put_args.add_argument("name", type=str, help="Name of the video is required", required=True)
video_put_args.add_argument("views", type=int, help="Views of the video", required=True)
video_put_args.add_argument("likes", type=int, help="Likes on the video", required=True)


# response = requests.put(base + "video/1", data_updated)
# set de record data_updated={}
video_update_args = reqparse.RequestParser()
video_update_args.add_argument("name", type=str, help="Name of the video is required")
video_update_args.add_argument("views", type=int, help="Views of the video")
video_update_args.add_argument("likes", type=int, help="Likes on the video")


resource_fields = {
	'id': fields.Integer,
	'name': fields.String,
	'views': fields.Integer,
	'likes': fields.Integer
}


# api
class Video(Resource):

	@marshal_with(resource_fields)
	def get(self, video_id):
		video = VideoModel.query.filter_by(id=video_id).first()
		if not video:
			abort(404, message="Could not find video with that id")

		return video


	@marshal_with(resource_fields)
	def put(self, video_id): # new VideoModel

        # requests.put(base + "video/1", data_new)
        # get data_new tu requests.put
		data_new = video_put_data_new.parse_data_new()

		video = VideoModel.query.filter_by(id=video_id).first()
		if video:

			abort(409, message="Video id taken...")

		video_new = VideoModel(id=video_id, name=data_new['name'], views=data_new['views'], likes=data_new['likes'])

		db.session.add(video_new)
		db.session.commit()

		return video, 201


	@marshal_with(resource_fields)
	def patch(self, video_id): # update VideoModel
		
        # requests.patch(base + "video/1", data_updated)
        # # get data_updated tu requests.patch
		data_updated = video_update_args.parse_args()

		video = VideoModel.query.filter_by(id=video_id).first()
		if not video:

			abort(404, message="Video doesn't exist, cannot update")

		if data_updated['name']:
			video.name = data_updated['name']

		if data_updated['views']:
			video.views = data_updated['views']

		if data_updated['likes']:
			video.likes = data_updated['likes']

		db.session.commit() # saved data

		return video


	def delete(self, video_id):
		abort_if_video_id_doesnt_exist(video_id)
		del videos[video_id]
		return '', 204


class HelloWorld(Resource):

    def get(self, name, old):
        return dict(name=name, old=old)


api.add_resource(HelloWorld, "/helloworld/<string:name>/<int:old>")

api.add_resource(Video, "/video/<int:video_id>")


if __name__ == "__main__":
	app.run(debug=True)