from tkinter import commondialog
from fastapi import Path
from fastapi_versioning import version
from fastapi.routing import APIRouter

from resource.v1.dto.cotacao_dto import CotacaoResponse
from service import cotacao_service


router = APIRouter(prefix="/cotacao")


@router.get("/{codigo}", response_model=CotacaoResponse)
@version(1)
async def consultar(codigo: int = Path(..., description="Código da cotação")):
    """
        Consultar cotação através do seu identificador
    """
    cotacao = cotacao_service.consultar(codigo)

    return CotacaoResponse(codigo=cotacao["codigo"], preco=cotacao["preco"], taxa=cotacao["taxa"])