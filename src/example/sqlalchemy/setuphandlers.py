from .model import Session, Base, Message

dummy_data = [
    {
        'title': u'test 1',
        'year': 2012,
    },
    {
        'title': u'test 2',
        'year': 2012,
    },
    {
        'title': u'test 3',
        'year': 2013,
    },
    {
        'title': u'test 4',
        'year': 2013,
    },
    {
        'title': u'test 5',
        'year': 2011,
    }
]


def setupVarious(context):
    if context.readDataFile('marker.txt') is None:
        return

    portal = context.getSite()
    # All'installazione creo tutte le tabelle necessarie al mio db
    session = Session()
    Base.metadata.create_all(session.bind)

    # e carico dei dati d'esempio
    for item in dummy_data:
        el = Message(**item)
        session.add(el)
        session.flush()
