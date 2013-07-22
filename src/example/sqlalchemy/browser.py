from zope.publisher.interfaces import IPublishTraverse
from zope.interface import implementer
from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from Products.Five.browser import BrowserView
from .model import Session
from .model import Message


# vedi: http://developer.plone.org/serving/traversing.html


@implementer(IPublishTraverse)
class MessageList(BrowserView):

    year = None
    message_id = None

    def __init__(self, context, request):
        super(MessageList, self).__init__(context, request)

        len_paths = len(self.request.path)
        if len_paths > 0:
            self.year = self.request.path[-1]

        if len_paths == 2:
            self.message_id = self.request.path[0]

    @property
    def _session(self):
        return Session()

    def publishTraverse(self, request, name):
        request['TraversalRequestNameStack'] = []
        return self

    def format_result(self, item):
        return {
            'title': item.title,
            'year': item.year,
            'id': item.message_id,
            'url': './messages/%s/%s' % (item.year, item.message_id),
            'year_url': './messages/%s' % item.year,
            'message_id': item.message_id
        }

    def results(self):
        query = self._session.query(Message)
        if self.year is not None:
            query = query.filter(Message.year == self.year)

        if self.message_id:
            query = query.filter(Message.message_id == self.message_id)
            if query.count() > 0:
                return self.format_result(query.one())
            return None

        results = []
        for item in query:
            results.append(self.format_result(item))
        return results

    def __call__(self):
        if self.message_id:
            return ViewPageTemplateFile("templates/show_message.pt")(self)
        return self.index()
