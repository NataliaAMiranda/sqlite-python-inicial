# Exemplos com Python3 e SQLite

Nesse repositório estão disponíveis pequenos exemplos em Python3 para acessar banco de dados SQLite.

No [Exemplo 01](ex01) é feito uso da biblioteca `sqlite3`. No exemplo é mostrado como conectar no banco e fazer consultas simples.

No [Exemplo 02](ex02) é feito uso da biblioteca `sqlalchemy`. Nesse exemplo, é apresentado do conceito de mapeamento objeto relacional (ORM) e a criação de classes Python a partir de um banco de dados já existente.

No [Exemplo 03](ex03) é mostrado como criar um esquema de banco a partir de classes Python com a biblioteca `sqlalchemy`.



## Preparando ambiente com virtualenv



```shell
python3 -m venv venv
source venv/bin/activate
pip install -r requirements.txt
```



## Executando

```shell
cd ex01
python3 exemplo01.py

cd ../ex02
python3 exemplo02.py

cd ../ex03
python3 exemplo03.py
```

