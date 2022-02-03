from pydantic import BaseModel
from typing import Optional

class CotacaoResponse(BaseModel):
    codigo: int
    preco: float
    taxa: Optional[float] = None

    class Config:
        schema_extra = {
            "example": {
                "codigo": 1,
                "preco": 50.00,
                "taxa": 3.2
            }
        }