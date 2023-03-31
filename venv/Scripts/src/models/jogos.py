from sqlalchemy import String, Column, Integer
from models.base import Base

# Criando a classe Jogo
class Jogo(Base):
    __tablename__ = 'jogos'
    id = Column(Integer, primary_key=True)
    nome = Column(String)
    console = Column(String)
    preco = Column(Integer)
    nota = Column(Integer)
 
# Criando o método construtor
    def __init__(self, nome, console, nota, preco):
        self.nome = nome
        self.console = console
        self.preco = preco
        self.nota = nota
        
# Criando o método __repr__ 
    def __repr__(self):
        return f'jogo {self.nome}, console {self.console}, preço {self.preco}, nota {self.nota}'