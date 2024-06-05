# criar um decorator @property











Restaurante.restaurante.append(self)









 @property
 ss Restaurante:
 restaurante=[]

    def __init__(self,nome,categoria):
        self.nome=nome
        self.categoria=categoria
        self.ativo=False
        
        Restaurante.restaurantes.append(self)

    def __str__(self):
        return f'{self.nome} | {self.categoria}'
 
    # 4 criar metodo para listar os restaurantes
        def 