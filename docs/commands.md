alembic init -t async migrations  -  инициализация алембика(при деплое приложения)
alembic revision --autogenerate -m "comment"  -  создание миграции
alembic upgrade heads  -  усвоение миграции