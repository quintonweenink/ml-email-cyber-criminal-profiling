from neomodel import StructuredNode, StringProperty, RelationshipTo, RelationshipFrom, config

config.DATABASE_URL = 'bolt://neo4j:admin@localhost:7687'

class EmailAddress(StructuredNode):
    name = StringProperty(unique_index=True)
    sent = RelationshipTo('Email', 'SENDER')
    received = RelationshipFrom('Email', 'RECIPIENT')

class Email(StructuredNode):
    name = StringProperty(unique_index=True)
    sender = RelationshipFrom('EmailAddress', 'SENDER')
    recipient = RelationshipTo('EmailAddress', 'RECIPIENT')


person = EmailAddress(name='Quinton').save()
person2 = EmailAddress(name='Bernhard').save()

email = Email(name='The best email').save()
person.sent.connect(email)
email.recipient.connect(person2)
person2.received.connect(email)