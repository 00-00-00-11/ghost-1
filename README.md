# Ghost
Advanced discord self bot that doesn't abuse Discord API!


`p3 -m app.py` to run the server`

### Celery + Redis
`brew install redis`
`brew services start redis`

`cd server`
`celery -A task.celery worker`