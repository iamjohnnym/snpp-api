#!venv/bin/python

from app import app, api

if __name__ == "__main__":
    app.debug = True
    #db.create_all(app=app)
    app.run(
            host="0.0.0.0",
            port=5000
            )
