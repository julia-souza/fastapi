from pydantic import BaseModel
from typing import Optional
from fastapi.encoders import jsonable_encoder
import json

class Entity(BaseModel):
    def classname(self):
        return 'entity'
    def check(self):
        return True
    def keygen(self):
        return 0
    def encode(self):
        return json.dumps(jsonable_encoder(self))    
