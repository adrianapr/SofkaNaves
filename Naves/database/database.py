from pymongo import MongoClient
MONGO_URI = 'mongodb://localhost:27017'

cliente = MongoClient(MONGO_URI)

db = cliente['sofkanaves']
collection= db['naves']

        
def guardarBaseDatos(document):
    collection.insert_one(document)


def buscarporId(query):
    result = collection.find_one(query)
    return result
        
def buscarPorTipo(query):
    return collection.find(query)
