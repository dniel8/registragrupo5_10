from typing import Generic, TypeVar, get_args
import certifi
import pymongo
import json
from bson import ObjectId

T = TypeVar('T')

# TODO add data validation and error handling
class InterfaceRepository(Generic[T]):

    def __int__(self):
        # Database connection
        ca = certifi.where()
        data_config = self.load_config_file()
        client = pymongo.MongoClient(
            data_config.get("db-connection"),
            tlsCAFile=ca
        )
        self.data_base = client[data_config.get("db-name")]

        # Get generic class name
        model_class = get_args(self.__orig_bases__[0])
        self.collection = model_class[0].__name__.lower()

    def load_config_file(self) -> dict:
        """

        :return:
        """
        with open("config.json", "r") as config:
            data = json.load(config)
        return data

    def find_all(self) -> list:
        current_collection = self.data_base[self.collection]
        dataset = []
        for document in current_collection.find({}):
            document['_id'] = document['_id'].__str__()
            document = self.transform_object_ids(document)
            document = self.get_values_db_ref(document)
            dataset.append(document)
        return dataset

    def find_by_id(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        document = current_collection.find_one({'_id': _id})
        document = self.get_values_db_ref(document)
        # If _id not found, document = None
        if document:
            document['_id'] = document['_id'].__str__()
        else:
            # Document not found
            document = {}
        return document

    def save(self, item: T) -> T:
        current_collection = self.data_base[self.collection]
        item = self.transform_refs(item)
        if hasattr(item, '_id') and item._id != "":
            # Update
            id_ = item._id
            _id = ObjectId(id_)
            delattr(item, '_id')
            item = item.__dict__()
            updated_item = {"$set": item}
            current_collection.update_one({'_id': _id}, updated_item)
        else:
            # Insert
            _id = current_collection.insert_one(item.__dict__)
            id_ = _id.inserted_id.__str__()
        return self.find_by_id(id_)

    # TODO check if update can be replaced by save
    def update(self, id_: str, item: T) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        item = item.__dict__
        updated_item = {"$set": item}
        document = current_collection.update_one({'_id': _id}, updated_item)
        return {"Updated count": document.matched_count}

    def delete(self, id_: str) -> dict:
        current_collection = self.data_base[self.collection]
        _id = ObjectId(id_)
        result = current_collection.delete_one({'_id': _id})
        return {"Deleted count": result.deleted_count}

    def query(self, query: dict) -> list:
        pass

    def query_aggregation(self, query: dict) -> list:
        pass

    def get_values_db_ref(self):
        pass

    def get_values_db_ref_from_list(self):
        pass

    def transform_object_ids(self):
        pass

    def transform_refs(self):
        pass

    def format_list(self):
        pass

    def object_to_db_ref(self):
        pass
