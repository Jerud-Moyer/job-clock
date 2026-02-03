## MIGRATION
### from /app 
- export FLASK_APP=":create_app"
- flask db migrate - to create migration(s)
- flask db upgrade - to run migrations

## FRONTEND
### Flask serves a static build of Vue app - from /frontend
- npm run build - build local then push

## SERVER
- gunicorn wsgi:app
