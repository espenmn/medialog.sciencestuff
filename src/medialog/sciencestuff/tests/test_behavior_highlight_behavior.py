# -*- coding: utf-8 -*-
from medialog.sciencestuff.behaviors.highlight_behavior import IHighlightBehaviorMarker
from medialog.sciencestuff.testing import MEDIALOG_SCIENCESTUFF_INTEGRATION_TESTING  # noqa
from plone.app.testing import setRoles
from plone.app.testing import TEST_USER_ID
from plone.behavior.interfaces import IBehavior
from zope.component import getUtility

import unittest


class HighlightBehaviorIntegrationTest(unittest.TestCase):

    layer = MEDIALOG_SCIENCESTUFF_INTEGRATION_TESTING

    def setUp(self):
        """Custom shared utility setup for tests."""
        self.portal = self.layer['portal']
        setRoles(self.portal, TEST_USER_ID, ['Manager'])

    def test_behavior_highlight_behavior(self):
        behavior = getUtility(IBehavior, 'medialog.sciencestuff.highlight_behavior')
        self.assertEqual(
            behavior.marker,
            IHighlightBehaviorMarker,
        )
