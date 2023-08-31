import uuid

from flask import Blueprint, jsonify, Response, request
from flask_pydantic import validate

from API.posts.models import Posts
from API.posts.schemas import BasePostSchema, CreatePostSchema, SuccessDeletePostSchema, SuccessUpdatePostSchema
from utils.serializers import Serializer

posts_api = Blueprint("posts_api", __name__)


@posts_api.route("/api/posts", methods=["POST"])
@validate()
def create_post(body: CreatePostSchema) -> tuple[Response, int] | tuple[BasePostSchema, int]:
    post = Posts.create(body)
    if not post:
        return jsonify(False), 400
    return BasePostSchema(**Serializer.to_dict(post)), 201


@posts_api.route("/api/posts/<uuid:post_id>", methods=["GET"])
@validate()
def get_post(post_id: uuid.UUID) -> tuple[Response, int] | tuple[BasePostSchema, int]:
    post = Posts.get(post_id)
    if not post:
        return jsonify(False), 400
    return BasePostSchema(**Serializer.to_dict(post)), 200


@posts_api.route("/api/posts", methods=["GET"])
def get_all_posts() -> tuple[Response, int] | tuple[list[dict], int]:
    posts = Posts.get_all()
    if not posts:
        return jsonify(False), 404
    return [BasePostSchema(**Serializer.to_dict(obj)).model_dump() for obj in posts], 200


@posts_api.route("/api/posts/<uuid:post_id>", methods=["PUT"])
@validate()
def update_post(post_id: uuid.UUID) -> tuple[Response, int] | tuple[SuccessUpdatePostSchema, int]:
    post = Posts.update(request.json, post_id)
    if not post:
        return jsonify(False), 404
    return SuccessUpdatePostSchema(**Serializer.to_dict(post)), 200


@posts_api.route("/api/posts/<uuid:post_id>", methods=["DELETE"])
@validate()
def delete_post(post_id: uuid.UUID) -> tuple[Response, int] | tuple[SuccessDeletePostSchema, int]:
    post = Posts.delete(post_id)
    if not post:
        return jsonify(False), 404
    return SuccessDeletePostSchema(**Serializer.to_dict(post)), 200




