from mongoengine import (Document,
                         EmbeddedDocument,
                         StringField,
                         ListField,
                         EmbeddedDocumentField)


class Item(EmbeddedDocument):
  color = StringField(max_length=30)
  size = StringField(max_length=30)


class Product(Document):
  name = StringField(max_length=200)
  brand = StringField(max_length=100)
  items = ListField(EmbeddedDocumentField(Item))
