class Estoque:
    
    def __init__(self, cod, descrição, fabricante, quantidade):

        self.cod = cod
        self.descrição = descrição
        self.fabricante = fabricante
        self.quantidade = quantidade
        self.favorito = False