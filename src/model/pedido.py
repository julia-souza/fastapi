from typing import Optional
from exceptions.custom import BadRequestException, NotFoundException
from model.entity import Entity
import dao.crud as crud
import json
import sys

class Pedido(Entity):   
    id_pedido: int 
    isbn: int
    quantity: int
    client: str
    status: bool

    def classname(self):
        return 'pedido'

    def check(self):

        read = crud.read(self.isbn, "book")

        read = json.loads(read)
        
        if(read['quantity'] >= self.quantity):
            self.status = True  #pedido aprovado!
            qtd = read['quantity']-self.quantity
            dados = {'quantity':qtd, 'reserverd':self.quantity,'id_pedido':self.id_pedido, 'client':self.client,'status':True}
            json_obj = json.dumps(dados)
            
            pedido = Pedido(id_pedido=self.id_pedido, isbn=self.isbn, quantity=qtd, client=self.client, status=self.status)
            print(pedido)

            #id_pedido=dict['id_pedido'],isbn=dict['isbn'],quantity=dict['quantity'],client=dict['client'], status=dict['status']
            
            crud.update(pedido, 'book')
        
        else:
            self.status = False #reserva
        return True
    
    def keygen(self):        
        return f"{self.classname()}/{self.id_pedido}"
         

