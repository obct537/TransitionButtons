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
        self.getControlPanel()
        element = browser.getControl('Site element.').value
        self.assertTrue(element != "")

    def test_saves(self):
        portal = self.layer['portal']
        browser = self.browser
        self.getControlPanel()
        browser.getControl('Site element.').value = u"empty"
        browser.getControl('Save').click()

        self.assertTrue(browser.getControl('Site element.').value == "empty")

    def test_viewlet_sees_changes(self):
        portal = self.layer['portal']
        browser = self.browser
        self.getControlPanel()
        browser.getControl('Site element.').value = u"empty"
        browser.getControl('Save').click()

        bv = self.buttonViewlet
        settings = bv.getSettings()

        self.assertTrue(settings.pageElement == u"empty")


