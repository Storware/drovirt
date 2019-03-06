import enum

from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import inspect

from drovirt.api.app import app
db = SQLAlchemy(app)


class SerializerMixin:
    def to_dict(self):
        """ Simple serializer """
        output = dict()
        for column in inspect(self).mapper.column_attrs:
            val = getattr(self, column.key)
            if isinstance(val, enum.Enum):
                output[column.key] = val.value
            else:
                output[column.key] = val
        return output

