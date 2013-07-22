# -*- coding: utf-8 -*-
import unittest2 as unittest
from zope.component import getUtility
from ..testing import FUNCTIONAL_LAYER
from ..model import Session
from ..model import Message


class TestSetup(unittest.TestCase):
    layer = FUNCTIONAL_LAYER

    def setUp(self):
        self.portal = self.layer['portal']
        self.request = self.layer['request']

    def test_db(self):
        # semplice test che verifica i dati salvati all'installazione
        # e visualizza l'uso della sessione
        session = Session()
        self.assertEqual(session.query(Message).count(), 5)

    def test_view(self):
        # questo attributo viene impostato dal publisher
        self.portal.REQUEST.path = []
        view = self.portal.restrictedTraverse('@@messages')
        self.assertEqual(len(view.results()),  5)

        self.portal.REQUEST.path = ['2012']
        view = self.portal.restrictedTraverse('@@messages')
        self.assertEqual(len(view.results()),  2)

        self.portal.REQUEST.path = ['1', '2012']
        view = self.portal.restrictedTraverse('@@messages')
        item = view.results()
        self.assertEqual(item['title'], u'test 1')
