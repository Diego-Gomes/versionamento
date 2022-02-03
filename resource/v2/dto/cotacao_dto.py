from pydantic import BaseModel
from typing import Optional

class ProponenteResponse(BaseModel):
    nome: str
    documento: Optional[str] = None

class CotacaoResponse(BaseModel):
    codigo: int
    preco: float
    taxa: Optional[float] = None
    proponente: ProponenteResponse

    class Config:
        schema_extra = {
            "example": {
                "codigo": 1,
                "preco": 50.00,
                "taxa": 3.2,
                "proponente": {
                    "nome": "Teste Teste",
                    "documento": "123456789-10"
                }
            }
        }