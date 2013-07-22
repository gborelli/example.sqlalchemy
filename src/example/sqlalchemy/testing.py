# -*- coding: utf-8 -*-
from plone.app.testing import PloneWithPackageLayer
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

import example.sqlalchemy


BASE_LAYER = PloneWithPackageLayer(
    zcml_package=example.sqlalchemy,
    zcml_filename='testing.zcml',
    gs_profile_id='example.sqlalchemy:default',
    name="BASE_LAYER")

INTEGRATION_LAYER = IntegrationTesting(
    bases=(BASE_LAYER, ),
    name="INTEGRATION_LAYER")

FUNCTIONAL_LAYER = FunctionalTesting(
    bases=(BASE_LAYER, ),
    name="FUNCTIONAL_LAYER")
