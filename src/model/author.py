from model.entity import Entity

class Author(Entity):    
    name: str
    cnpj: int
    def classname(self):
        return 'author'
    def check(self):
        return self.cnpj > 0
    def keygen(self):        
        return f"{self.classname()}/{self.cnpj}"