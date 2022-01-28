# Estoque

Controle de estoque, inspirado no tutorial de Estoque do Regis do Python.


## Como rodar o projeto?

* Clone esse repositório.
* Crie um virtualenv com Python 3.
* Ative o virtualenv.
* Instale as dependências.
* Rode as migrações.
* Rode os testes.
* Rode o projeto.

```bash
git clone https://github.com/orlandosaraivajr/estoque.git
cd estoque
python3 -m venv .venv
source .venv/bin/activate
pip install -r requirements.txt
cd projeto
python -m coverage run --source='.' manage.py test
coverage report
coverage html
python manage.py migrate
python manage.py runserver
```

## Links

[Canal do Regis](https://www.youtube.com/watch?v=b7rInOLJ43M&list=PLsGCdfxkV9uqj9DwI6Y72JyvXeA-9mAjc)

[Link github projeto original](https://github.com/rg3915/estoque)

