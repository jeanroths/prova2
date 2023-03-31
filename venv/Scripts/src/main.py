from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker
from models.base import Base
from models.jogos import Jogo

# Criando o banco de dados
engine = create_engine('sqlite:///jogos.db', echo=True)

# Criando uma sessão
Session = sessionmaker(bind=engine)
session= Session()

# Criando as tabelas
Base.metadata.create_all(engine)

# Inserindo dados
j1 = Jogo(nome = 'DEAD SPACE REMAKE', console = 'PS5', preco = 350, nota = 10)
j2 = Jogo(nome = 'FORSPOKEN', console = 'PC', preco = 299, nota = 8)
j3 = Jogo(nome = 'DEAD ISLAND 2', console = 'PS5', preco = 350, nota = 10)
j4 = Jogo(nome = 'HOGWARTS LEGACY', console = 'PC', preco = 219, nota = 7)
j5 = Jogo(nome = 'WILD HEARTS', console = 'Xbox Series', preco = 350, nota = 7)
j6 = Jogo(nome = 'RESIDENT EVIL 4', console = 'PS5', preco = 289, nota = 10)
j7 = Jogo(nome = 'THE LEGEND OF ZELDA: TEARS OF THE KINGDOM', console = 'Switch', preco = 350, nota = 10)

# Adicionando os dados
session.add(j1)
session.add(j2)
session.add(j3)
session.add(j4)
session.add(j5)
session.add(j6)
session.add(j7)

# Salvando os dados
session.commit()

# Consultando os dados
jogos = session.query(Jogo).all()
print(jogos)

