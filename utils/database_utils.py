import uuid
from typing import List, Type

from pydantic import BaseModel

from API import db
import logging


logging.basicConfig(
    level=logging.ERROR,
    filename="logs.log",
    filemode="a",
    format="%(asctime)s %(levelname)s %(message)s",
)


class DataBase:
    """Class for db sessions which can work with any model"""

    @staticmethod
    def create(
        ModelClass: Type["ModelClass"], body: BaseModel
    ) -> Type["ModelClass"] | bool:
        """
        Create any object in necessary model

        :param ModelClass: ModelClass necessary model
        :param body: object of Type[BaseModel]
        :return: if success - ModelClass, else False
        """
        try:
            obj = ModelClass(**body.model_dump())
            db.session.add(obj)
            db.session.commit()
            return obj
        except Exception as exc:
            logging.error(exc, exc_info=True)
            db.session.rollback()
            return False

    @staticmethod
    def get(
        ModelClass: Type["ModelClass"], object_id: uuid.UUID
    ) -> Type["ModelClass"] | bool:
        """
        Get one row by id

        :param ModelClass: ModelClass necessary model
        :param object_id: id of row in db
        :return: if success - ModelClass, else False
        """
        try:
            return ModelClass.query.get(object_id)
        except Exception as exc:
            logging.error(exc, exc_info=True)
            return False

    @staticmethod
    def get_all(ModelClass: Type["ModelClass"]) -> List[Type["ModelClass"]] | bool:
        """
        Get all rows of model

        :param ModelClass: ModelClass necessary model
        :return: if success - List[ModelClass], else False
        """
        try:
            return ModelClass.query.all()
        except Exception as exc:
            logging.error(exc, exc_info=True)
            return False

    @staticmethod
    def update(
        ModelClass: Type["ModelClass"], body: dict, object_id: uuid.UUID
    ) -> Type["ModelClass"] | bool:
        """
        Update row by id

        :param ModelClass: ModelClass necessary model
        :param body: object of Type[BaseModel]
        :param object_id: id of row in db
        :return: if success - ModelClass, else False
        """
        try:
            obj = ModelClass.query.get(object_id)
            if not obj:
                return False

            for key, value in body.items():
                setattr(obj, key, value)
            db.session.commit()
            return obj
        except Exception as exc:
            logging.error(exc, exc_info=True)
            db.session.rollback()
            return False

    @staticmethod
    def delete(
        ModelClass: Type["ModelClass"], object_id: uuid.UUID
    ) -> Type["ModelClass"] | bool:
        """
        Delete row by id

        :param ModelClass: ModelClass necessary model
        :param object_id: id of row in db
        :return: if success - ModelClass, else False
        """
        try:
            obj = ModelClass.query.get(object_id)
            if not obj:
                return False

            db.session.delete(obj)
            db.session.commit()
            return obj
        except Exception as exc:
            logging.error(exc, exc_info=True)
            db.session.rollback()
            return False
