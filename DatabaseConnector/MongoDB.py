import discord
from DatabaseConnector.Database import DatabaseService

class MongoService(DatabaseService):

    def __init__(self, mongo_instance, database_name, collection_name) -> None:
        self.mongo_instance = mongo_instance
        self.cluster = self.mongo_instance[database_name]        
        self.collection = self.cluster[collection_name]

    def insert_one(self, discord_message) -> bool :
        try:
            data = MongoService.transform_data(discord_message)
            self.collection.insert_one(data)
            return True

        # will back
        except Exception as e:
            raise e
    
    # def insert_many(self, discord_message_list) -> bool:
    #     raise NotImplementedError()
        # try:
        #     self.collection.insert_many(data)
        #     return True
        # except Exception as e:
        #     raise e

    def close_connection(self) -> None:
        self.mongo_instance.close()

    @staticmethod
    def transform_data(discord_message):
        return {"channel" : discord_message.channel.name,
                "user" : discord_message.author.name,
                "date_time" : discord_message.created_at,
                "message_content" : discord_message.content}

