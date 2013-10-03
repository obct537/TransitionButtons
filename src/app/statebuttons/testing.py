from plone.app.testing import PloneSandboxLayer
from plone.app.testing import applyProfile
from plone.app.testing import PLONE_FIXTURE
from plone.app.testing import IntegrationTesting
from plone.app.testing import FunctionalTesting

from plone.testing import z2

from zope.configuration import xmlconfig


class AppstatebuttonsLayer(PloneSandboxLayer):

    defaultBases = (PLONE_FIXTURE,)

    def setUpZope(self, app, configurationContext):
        # Load ZCML
        import app.statebuttons
        xmlconfig.file(
            'configure.zcml',
            app.statebuttons,
            context=configurationContext
        )

        # Install products that use an old-style initialize() function
        #z2.installProduct(app, 'Products.PloneFormGen')

#    def tearDownZope(self, app):
#        # Uninstall products installed above
#        z2.uninstallProduct(app, 'Products.PloneFormGen')


APP_STATEBUTTONS_FIXTURE = AppstatebuttonsLayer()
APP_STATEBUTTONS_INTEGRATION_TESTING = IntegrationTesting(
    bases=(APP_STATEBUTTONS_FIXTURE,),
    name="AppstatebuttonsLayer:Integration"
)
APP_STATEBUTTONS_FUNCTIONAL_TESTING = FunctionalTesting(
    bases=(APP_STATEBUTTONS_FIXTURE, z2.ZSERVER_FIXTURE),
    name="AppstatebuttonsLayer:Functional"
)
