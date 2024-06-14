import sqlalchemy  # Importa SQLAlchemy para trabalhar com bancos de dados
from sqlalchemy import create_engine  # Importa a função create_engine para criar uma engine de banco de dados
import pandas as pd  # Importa Pandas para manipulação de dados

# Cria uma engine de banco de dados SQLite em memória
engine = create_engine('sqlite:///:memory:')

# URL do arquivo CSV que contém os dados dos clientes
url = 'https://raw.githubusercontent.com/alura-cursos/Pandas/main/clientes_banco.csv'

# Lê os dados do arquivo CSV para um dataframe Pandas
dados = pd.read_csv(url)

# Imprime os dados lidos do arquivo CSV
print(dados)

# Salva os dados do dataframe 'dados' na tabela 'clientes' do banco de dados SQLite
dados.to_sql('clientes', engine, index=False)

# Lê os dados da tabela 'clientes' do banco de dados SQLite para um dataframe Pandas
pd.read_sql_table('clientes', engine)

# Define uma query SQL para atualizar o valor do campo 'Rendimento_anual' para um cliente específico
query = 'UPDATE clientes SET Rendimento_anual=300000.0 WHERE ID_Cliente=6840104'

# Executa a query SQL de atualização usando a conexão com a engine
with engine.connect() as conn:
    conn.execute(query)

# Define uma query SQL para excluir um cliente específico da tabela 'clientes'
query = 'DELETE FROM clientes WHERE ID_Cliente=5008809'

# Executa a query SQL de exclusão usando a conexão com a engine
with engine.connect() as conn:
    conn.execute(query)

# Define uma query SQL para inserir um novo cliente na tabela 'clientes'
query = 'INSERT INTO clientes (ID_Cliente, Idade, Grau_escolaridade, Estado_civil, ' \
        'Tamanho_familia, Categoria_de_renda, Ocupacao, Anos_empregado, ' \
        'Rendimento_anual, Tem_carro, Moradia) ' \
        'VALUES (6850985, 33, "Doutorado", "Solteiro", 1, "Empregado", "TI", ' \
        '2, 290000, 0, "Casa/apartamento próprio")'

# Executa a query SQL de inserção usando a conexão com a engine
with engine.connect() as conn:
    conn.execute(query)

# Lê novamente os dados da tabela 'clientes' do banco de dados SQLite para um dataframe Pandas
pd.read_sql_table('clientes', engine)

