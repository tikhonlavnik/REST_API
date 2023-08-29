from typing import Type, Union, List

from pydantic import BaseModel

from API import db


class DataBase:
    """ Class for db sessions which can work with any model """
    @staticmethod
    def create(ModelClass: Type[BaseModel], body: BaseModel) -> Type["ModelClass"] | bool:
        """
        Create any object in necessary model

        :param ModelClass: Type[BaseModel] necessary model
        :param body: object of
        :return: if success - ModelClass, else False
        """
        try:
            obj = ModelClass(**body.model_dump())
            db.session.add(obj)
            db.session.commit()
            return obj
        except:
            db.session.rollback()
            return False

    @staticmethod
    def get(ModelClass: Type[BaseModel], object_id: int) -> Type["ModelClass"] | bool:
        """
        Get one row by id

        :param ModelClass: Type[BaseModel] necessary model
        :param object_id: id of row in db
        :return: if success - ModelClass, else False
        """
        try:
            return ModelClass.query.get(object_id)
        except:
            return False

    @staticmethod
    def get_all(ModelClass: Type[BaseModel]) -> List["ModelClass"] | bool:
        """
        Get all rows of model

        :param ModelClass: Type[BaseModel] necessary model
        :return: if success - List[ModelClass], else False
        """
        try:
            return ModelClass.query.all()
        except:
            return False

    @staticmethod
    def update(ModelClass: Type[BaseModel], body: dict, object_id: int) -> Type["ModelClass"] | bool:
        """
        Update row by id

        :param ModelClass: Type[BaseModel] necessary model
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
        except:
            db.session.rollback()
            return False

    @staticmethod
    def delete(ModelClass: Type[BaseModel], object_id: int) -> Type["ModelClass"] | bool:
        try:
            obj = ModelClass.query.get(object_id)
            if not obj:
                return False

            db.session.delete(obj)
            db.session.commit()
            return obj
        except:
            db.session.rollback()
            return False
