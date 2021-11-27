from abc import ABC

class Config (ABC):
    class Database (ABC):
        path = "data/database.nosql"
        _type = "disk"
