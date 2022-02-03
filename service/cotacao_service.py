cotacoes = {
            "1": {"codigo": 1 , "preco": 10, "taxa": 2.2, "proponente": {"nome": "Diego Farias", "documento": "123456789-10"}},
            "2": {"codigo": 2 , "preco": 20, "taxa": 1.3, "proponente": {"nome": "Jóse Almeida", "documento": "123456789-10"}},
            "3": {"codigo": 3 , "preco": 5, "taxa": 0.4, "proponente": {"nome": "Fernando Romero", "documento": "123456789-10"}}
            }

def consultar(codigo:int) :
    return cotacoes[str(codigo)]