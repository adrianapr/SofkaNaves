from pymongo import MongoClient
import os

ipBaseDatos= os.environ.get('DB_HOST')
print(ipBaseDatos)

if ipBaseDatos == None:
   MONGO_URI = 'mongodb://localhost:27017'
else:
    MONGO_URI = 'mongodb://'+ipBaseDatos+':27017'

print(MONGO_URI)

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
