from pymongo import MongoClient
MONGO_URI = 'mongodb://localhost:27017'

cliente = MongoClient(MONGO_URI)

db = cliente['sofkanaves']
collection= db['naves']



# results = collection.find({"nombre_nave":"Hola"})

# for r in results:
#     print(r)

# result = collection.find_one({"nombre_nave":"Saturno"})
# print(result)
# result = collection.delete_many({})
