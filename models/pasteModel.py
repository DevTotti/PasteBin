from mongoengine import Document, StringField, ListField, IntField, DateTimeField, URLField, BooleanField
import datetime

class Paste(Document):
    text = StringField(required=True)
    expiration = IntField(min_value=600, default=288400000, required=False)
    visibility = BooleanField(required=False, default=False)
    password = StringField(required=False, default='', min_length=2)
    name = StringField(required=True, max_length=100)
    paste_code = StringField(required=True, max_length=7)
    created = DateTimeField(default=datetime.datetime.now())


# class ShortCode(Document):
#     code = StringField(required=True, max_length=7)
#     created = DateTimeField(default=datetime.datetime.now)


class DeleteExpired(Document):
    date = StringField(required=True)
    expiry = IntField(required=True)
    obj_id = StringField(required=True)


