from pydoc import classname
from model.entity import Entity
from exceptions.custom import NotFoundException, BadRequestException, AlreadyExistsException
import redis, json

def connection():
    return redis.Redis(host='localhost', port=6379, db=0)

def create(entity: Entity):
    if(entity.check() == False): raise BadRequestException(entity.classname())
    if(connection().get(entity.keygen()) == None): 
        connection().set(entity.keygen(), entity.encode())
    else: raise AlreadyExistsException(entity.classname())
def read(key: int, classname: str):    
    data = connection().get(f"{classname}/{key}")
    if(data == None): raise NotFoundException(classname)
    else: return data
def list(classname: str, ini: int, offset: int):
    list = []
    for key in connection().scan_iter(f"{classname}/*", ini+offset):
        list.append(json.loads(connection().get(key)))
    return list[ini:ini+offset]
def delete(key: int, classname: str):    
    data = connection().get(f"{classname}/{key}")
    if(data == None): raise NotFoundException(classname)
    else: connection().delete(f"{classname}/{key}")
def update(entity: Entity, key: int):    
    if(entity.check() == False or entity.keygen() != f"{entity.classname()}/{key}"):
        raise BadRequestException(entity.classname())
    if(connection().get(entity.keygen()) == None): 
        raise NotFoundException(entity.classname())
    else: connection().set(entity.keygen(), entity.encode())
