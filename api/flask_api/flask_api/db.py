from sqlalchemy import *
from sqlalchemy.orm import mapper, scoped_session, sessionmaker


engine = create_engine('sqlite:///./test.db', convert_unicode=True)
metadata = MetaData(bind=engine)
db_session = scoped_session(sessionmaker(autocommit=False,
                                         autoflush=False,
                                         bind=engine))


messages = Table('messages', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('message',Text, nullable=False),
                 Column('time', DATETIME, nullable = False),
                 Column('sender', String(255), nullable = False),
                 Column('recipient', String(255), nullable = False),
                 Column('isSpam', BOOLEAN, nullable = False)
                 #Column('group', Text, nullable = True)
                 )

class Messages(object):
    query = db_session.query_property()

    def __init__(self,  
                 message=None,
                 time=None,
                 sender=None,
                 recipient=None,
                 isSpam=None
                 ):
        self.message = message
        self.time=time
        self.sender=sender
        self.recipient=recipient
        self.isSpam = isSpam

    def __repr__(self):
        return '<id:{} sender:{}>'.format(self.id, self.sender)
mapper(Messages,messages)

models = Table('models', metadata,
               Column('id', Integer, primary_key=True),
               Column('sender', String(255), nullable = False),
               Column('recipient', String(255), nullable = False),
               Column('model', PickleType, nullable=False)
               )
class Models(object):
    query = db_session.query_property()

    def __init__(self,
                 sender=None,
                 recipient=None,
                 model=None):
        self.sender = sender
        self.recipient = recipient
        self.model = model

    def __repr__(self):
        return '<sender:{} recipient:{}>'.format(self.sender, self.recipient)
mapper(Models, models)

emotions = Table('emotions', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('msg_id', Integer, nullable = False),
                 Column('emotion', Text, nullable = False),
                 Column('magnitude', FLOAT, nullable = False)
                 )
class Emotions(object):
    query = db_session.query_property()

    def __init__(self,
                 mid=None,
                 emotion=None,
                 magnitude=None):
        self.mid= mid
        self.emotion = emotion
        self.magnitude = magnitude

    def __repr__(self):
        return '<id:{} mag:{}>'.format(self.mid, self.magnitude)

mapper(Emotions, emotions)

entities = Table('entities', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('msg_id', Integer, nullable=False),
                 Column('entity', Text, nullable = False),
                 Column('sentiment', Text, nullable = False),
                 Column('type', Text, nullable = False),
                 Column('salience', Float, nullable = False),
                 Column('metadata', Text, nullable = False)
                 )

class Entities(object):
    query = db_session.query_property()

    def __init__(self,
                 mid=None,
                 entity=None,
                 sentiment=None,
                 etype=None,
                 salience=None,
                 metadata=None):
        self.mid= mid
        self.entity = entity
        self.sentiment = sentiment
        self.etype=etype
        self.salience = salience
        self.metadata = metadata


    def __repr__(self):
        return '<mid:{}>'.format(self.mid)

mapper(Entities, entities)


