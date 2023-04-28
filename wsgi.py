"poetry run python3 wsgi.py"

from my_blog.app import create_app

app = create_app()
app.run(
    host='0.0.0.0',
    debug=True

)
