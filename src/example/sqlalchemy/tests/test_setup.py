# -*- coding: utf-8 -*-
import unittest2 as unittest
from zope.component import getUtility
from ..testing import INTEGRATION_LAYER
from ..model import Session
from ..model import Message


class TestSetup(unittest.TestCase):
    layer = INTEGRATION_LAYER

    def setUp(self):
        self.portal = self.layer['portal']

    def test_db(self):
        # semplice test che verifica i dati salvati all'installazione
        # e spiega l'uso della sessione
        session = Session()
        self.assertEqual(session.query(Message).count(), 5)

    def test_view(self):
        view = self.portal.restrictedTraverse('@@messages')

        res = [i for i in view.results()]
        self.assertEqual(res,  5)
        import pdb; pdb.set_trace( )
