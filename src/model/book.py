from typing import Optional
from exceptions.custom import BadRequestException, NotFoundException
from model.entity import Entity
import dao.crud as crud

class Book(Entity):    
    name: Optional[str] = None
    isbn: int
    quantity: Optional[int] = 0
    reserved: Optional[int] = 0
    author: int
    def classname(self):
        return 'book'
    def check(self):
        fields_validation = self.isbn > 0 and self.quantity >=0 and self.reserved >= 0 and self.author > 0
        if(fields_validation == False): False
        try: crud.read(self.author, 'author')
        except NotFoundException: raise BadRequestException(self.classname())
        return True
    def keygen(self):        
        return f"{self.classname()}/{self.isbn}"