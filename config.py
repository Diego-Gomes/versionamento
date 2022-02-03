from resource.v1.cotacao import router as cotacao_router_v1

def configurar_rotas(app):

    app.include_router(cotacao_router_v1)

    return app