from sqlalchemy.orm import Session

from .app_setup import create_app, db, cache

app = create_app()



from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

from .model import Data


@app.route("/")
@cache.cached(timeout=5)
def index():
    session: 'Session' = db.session
    return session.query(Data.time_updated).order_by(-Data.time_updated).first()[0].isoformat()



if __name__ == '__main__':
    app.run(host='192.168.88.23', port=8080, debug=True)
