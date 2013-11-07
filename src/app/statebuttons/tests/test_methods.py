import unittest2 as unittest
from plone.app.testing import setRoles, login, TEST_USER_NAME

from app.statebuttons.testing import BaseTest

from Products.CMFCore.utils import getToolByName
from zope.component import queryMultiAdapter
from zope.viewlet.interfaces import IViewletManager
from Products.Five.browser import BrowserView as View

from app.statebuttons.browser.viewlets import ButtonViewlet
import Products.DCWorkflow as wftool

from app.statebuttons.testing import \
    APP_STATEBUTTONS_FUNCTIONAL_TESTING


class TestMethods(BaseTest):

    layer = APP_STATEBUTTONS_FUNCTIONAL_TESTING

    def test_installed(self):
    	portal = self.layer['portal']
    	installer = getToolByName(portal, 'portal_quickinstaller')
    	self.assertTrue(installer.isProductInstalled('app.statebuttons'))

    def test_js(self):
    	portal = self.layer['portal']
    	js_reg = getToolByName(portal, 'portal_javascripts')
    	self.assertTrue('transitionbuttons.js' in js_reg.getResourceIds())

    def test_isPanelEnabled(self):
        portal = self.layer['portal']
        login(portal, TEST_USER_NAME)

        bv = self.buttonViewlet
        isEnabled = bv.isPanelEnabled()
        self.assertTrue(isEnabled)

    def test_getWFStateself(self):
        portal = self.layer['portal']
        login(portal, TEST_USER_NAME)

        bv = self.buttonViewlet
        state = bv.getWFState()
        self.assertEqual(state, 'private')

    def test_getSettings(self):
        portal = self.layer['portal']
        login(portal, TEST_USER_NAME)

        bv = self.buttonViewlet
        settings = bv.getSettings()
        self.assertIsNotNone(settings)

    def test_getStateDescription(self):
        portal = self.layer['portal']
        login(portal, TEST_USER_NAME)
        #import pdb; pdb.set_trace()

        bv = self.buttonViewlet
        desc = bv.getStateDescription()
        self.assertEqual(desc, 'Can only be seen and edited by the owner.')

    def test_setJson(self):
        portal = self.layer['portal']
        login(portal, TEST_USER_NAME)

        bv = self.buttonViewlet
        json = bv.setJson()
        self.assertIsNotNone(json)

    def test_viewletPresent(self):
        portal = self.layer['portal']
        login(portal, TEST_USER_NAME)

        bv = self.buttonViewlet
        docUrl = self.doc.absolute_url()
        browser = self.browser
        browser.open(docUrl)
        self.assertTrue('js_info' in browser.contents)



