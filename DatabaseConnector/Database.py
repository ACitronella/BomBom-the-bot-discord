

# parents class fora all basic database service
class DatabaseService:
    
    def __init__(self):
        raise NotImplementedError()

    def insert_one(self, data) -> bool:
        raise NotImplementedError()

    def insert_many(self, data) -> bool:
        raise NotImplementedError()

    def close_connection(self):
        raise NotImplementedError()