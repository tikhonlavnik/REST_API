from typing import Type, List


class Serializer:
    """ Serialize any class to dict """
    @staticmethod
    def to_dict(obj: Type["Model"]) -> dict:
        if not obj:
            return {}

        result = {}
        for field in obj.__table__.columns:
            result[field.name] = getattr(obj, field.name)
        return result

    @staticmethod
    def to_dict_list(objects: List[Type["Model"]]) -> List[dict]:
        return [Serializer.to_dict(obj) for obj in objects]
