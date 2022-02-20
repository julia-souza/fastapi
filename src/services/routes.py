from fastapi import FastAPI, status, Response

from model.book import Book
from model.author import Author

import dao.crud as crud

def prefix(): 
    return '/fastapi/sd/'
def services():
    return {'author': Author, 'book': Book}
def create_fastapi_meta():
    return FastAPI(
        title="fastapi-sd",
        description="Trabalho de Sistemas Distribuidos utilizando FastAPI",
        version="0.0.1",
        contact={
            "name": "Felipe e Júlia",        
        },
        docs_url="/sd/documentation",
        tags_metadata = [
            {
                "name": "author",
            },
            {
                "name": "book",
            },
            {
                "name": "order",
            },          
        ]
    )
def create_entity_crud_routes(app: FastAPI, route: str):
    @app.get(
        path=prefix()+route+"/{key}", 
        tags=[route], 
        responses={404: {"description": f"The {route} was not found"}}
    )
    async def read(key: int):
        return Response(content=crud.read(key, route), media_type="application/json")
                
    @app.get(prefix()+route+"/", tags=[route])
    async def list(ini: int = 0, offset: int = 10):
        return crud.list(route, ini, offset)
        
    @app.post(prefix()+route+"/", tags=[route], status_code = status.HTTP_204_NO_CONTENT)
    async def create(data: services()[route]):
        crud.create(data)
        return Response(content=None, media_type=None, status_code=status.HTTP_204_NO_CONTENT)

    @app.put(prefix()+route+"/{key}", tags=[route], status_code = status.HTTP_204_NO_CONTENT)
    async def update(key: int, data: services()[route]):
        crud.update(data, key)
        return Response(content=None, media_type=None, status_code=status.HTTP_204_NO_CONTENT)
    
    @app.delete(prefix()+route+"/{key}", tags=[route], status_code = status.HTTP_204_NO_CONTENT)
    async def delete(key: int):
        crud.delete(key, route)
        return Response(content=None, media_type=None, status_code=status.HTTP_204_NO_CONTENT)
    return app

def create_user_case_route_purchase(app):
    @app.post(prefix()+"book/purchase", tags=['order'], status_code = status.HTTP_204_NO_CONTENT)
    async def purchase():        
        # Implementar registro da compra para posterior consulta e disparar thread para verificação de disponibilidade em estoque
        return {}
    return app
def create_user_case_route_view_order(app):
    @app.get(prefix()+"order/", tags=['order'], status_code = status.HTTP_204_NO_CONTENT)
    async def view_order():        
        # Implementar busca por id do pedido mostrando status de entrega
        return {}
    return app

def create_fastapi():
    app = create_fastapi_meta()
    for api in services():
        app = create_entity_crud_routes(app, api)
    app = create_user_case_route_purchase(app)
    app = create_user_case_route_view_order(app)
    return app