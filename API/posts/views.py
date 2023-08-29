from flask import Blueprint, jsonify, request

from API.posts.schemas import BasePostSchema

posts_api = Blueprint("posts_api", __name__)


@posts_api.route("/api/posts", methods=["GET"])
def get_posts():
    return jsonify(success=True)


@posts_api.route("/api/posts", methods=["POST"])
def create_post():
    body = BasePostSchema(**request.json)
    return jsonify(True)

