
from flask_sqlalchemy import SQLAlchemy

from drovirt.api.rest import app

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://drovirt@/drovirt'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

