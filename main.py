from litedb import database, DiskDatabase, MemoryDatabase

def run (Config: object) -> database:
    if Config.Database._type == "disk":
        database = DiskDatabase(Config.Database.path)
    else:
        databse = MemoryDatabase()
    print("Running...")
    return database
