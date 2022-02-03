from fastapi import Path
from fastapi_versioning import version
from fastapi.routing import APIRouter

from resource.v2.dto.cotacao_dto import CotacaoResponse, ProponenteResponse
from service import cotacao_service

router = APIRouter(prefix="/cotacao")


@router.get("/{codigo}", response_model=CotacaoResponse )
@version(2)
def consultar(codigo: int = Path(..., description="Código da cotação")):
        """
        Consultar cotação através do seu identificador
        
        """   
        cotacao = cotacao_service.consultar(codigo)

        proponenteResponse = ProponenteResponse(
                nome=cotacao["proponente"]["nome"],
                documento=cotacao["proponente"]["documento"]
        )

        return CotacaoResponse( codigo=cotacao["codigo"], 
                                preco=cotacao["preco"], 
                                taxa=cotacao["taxa"], 
                                proponente=proponenteResponse)
