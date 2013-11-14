from plone.app.users.browser.personalpreferences import PersonalPreferencesPanelAdapter
from app.statebuttons.userdataschema import IEnhancedUserDataSchema
from zope.interface import implements

class EnhancedUserDataPanelAdapter(PersonalPreferencesPanelAdapter):
    """
    """
    implements(IEnhancedUserDataSchema)

    def get_buttonEnabled(self):
        return self.context.getProperty('buttonsEnabled', '')
    def set_buttonsEnabled(self, value):
        return self.context.setMemberProperties({'buttonsEnabled': value})
    buttonsEnabled = property(get_buttonEnabled, set_buttonsEnabled)