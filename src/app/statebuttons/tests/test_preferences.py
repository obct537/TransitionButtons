import unittest2 as unittest
from plone.app.testing import setRoles, login, TEST_USER_NAME

from app.statebuttons.testing import BaseTest
from app.statebuttons.controlpanel import ButtonSettingsControlPanel as Base
from Products.CMFCore.utils import getToolByName
from Products.Five.browser import BrowserView as View

from app.statebuttons.testing import \
    APP_STATEBUTTONS_FUNCTIONAL_TESTING


class TestControlPanel(BaseTest):

    layer = APP_STATEBUTTONS_FUNCTIONAL_TESTING

    def test_exists(self):
        portal = self.layer['portal']
        browser = self.browser
        self.getPreferencesPanel()
        element = browser.getControl('Transition button widget.').value
        self.assertIsNotNone(element)
