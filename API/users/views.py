import uuid

from flask import Blueprint, jsonify, Response, request

from API.users.models import Users
from API.users.schemas import (
    CreateUserSchema,
    BaseUserSchema,
    SuccessUpdateUserSchema,
    SuccessDeleteUserSchema,
)

from flask_pydantic import validate

from utils.serializers import Serializer


users_api = Blueprint("users_api", __name__)


@users_api.route("/api/users", methods=["POST"])
@validate()
def create_user(
    body: CreateUserSchema,
) -> tuple[Response, int] | tuple[BaseUserSchema, int]:
    user = Users.create(body)
    if not user:
        return jsonify(False), 400
    return BaseUserSchema(**Serializer.to_dict(user)), 201


@users_api.route("/api/users/<uuid:user_id>", methods=["GET"])
@validate()
def get_user(user_id: uuid.UUID) -> tuple[Response, int] | tuple[BaseUserSchema, int]:
    user = Users.get(user_id)
    if not user:
        return jsonify(False), 404
    return BaseUserSchema(**Serializer.to_dict(user)), 200


@users_api.route("/api/users", methods=["GET"])
def get_all_users() -> tuple[Response, int] | tuple[list[dict], int]:
    users = Users.get_all()
    if not users:
        return jsonify(False), 404
    return [
        BaseUserSchema(**Serializer.to_dict(obj)).model_dump() for obj in users
    ], 200


@users_api.route("/api/users/<uuid:user_id>", methods=["PUT"])
@validate()
def update_user(
    user_id: uuid.UUID,
) -> tuple[Response, int] | tuple[SuccessUpdateUserSchema, int]:
    user = Users.update(request.json, user_id)
    if not user:
        return jsonify(False), 404
    return SuccessUpdateUserSchema(**Serializer.to_dict(user)), 200


@users_api.route("/api/users/<uuid:user_id>", methods=["DELETE"])
@validate()
def delete_user(
    user_id: uuid.UUID,
) -> tuple[Response, int] | tuple[SuccessDeleteUserSchema, int]:
    user = Users.delete(user_id)
    if not user:
        return jsonify(False), 404
    return SuccessDeleteUserSchema(**Serializer.to_dict(user)), 200
