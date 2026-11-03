# Minha Trajetória no Futebol (blog em Django)

Blog pessoal sobre a minha trajetória no futebol, desenvolvido com Django para a disciplina
PMR3304 - Sistemas de Informação (Escola Politécnica da USP).

Funcionalidades: CRUD de posts, comentários de usuários cadastrados e categorias de posts.

## Como executar localmente

```bash
python -m venv .venv
.venv\Scripts\activate          # Linux/macOS: source .venv/bin/activate
pip install -r requirements.txt
python manage.py migrate
python manage.py shell -c "exec(open('populate_db.py', encoding='utf-8').read())"   # categorias, posts e comentários
python manage.py createsuperuser
python manage.py runserver
```

O site fica em http://127.0.0.1:8000/ e a administração em http://127.0.0.1:8000/admin/.

## Implantação (Render)

- Build command: `./build.sh`
- Start command: `gunicorn config.wsgi`
- Variáveis de ambiente: `SECRET_KEY`, `PYTHON_VERSION`, `DJANGO_SUPERUSER_USERNAME`,
  `DJANGO_SUPERUSER_EMAIL` e `DJANGO_SUPERUSER_PASSWORD`.
- Opcional: `DATABASE_URL` para usar um banco PostgreSQL do Render (sem ela, usa SQLite).
