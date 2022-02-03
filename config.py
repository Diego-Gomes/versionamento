from resource.v1.cotacao import router as cotacao_router_v1
from resource.v2.cotacao import router as cotacao_router_v2

def configurar_rotas(app):

    app.include_router(cotacao_router_v1)
    app.include_router(cotacao_router_v2)
    
    return app