from zope.interface import Interface
from zope import schema

class IMessage(Interface):

    message_id = schema.Int(
        title=u'',
        description=u'',
        required=True,
    )

    year = schema.Int(
        title=u'',
        description=u'',
        required=True,
    )

    title = schema.TextLine(
        title=u'',
        description=u'',
        required=True,
    )
