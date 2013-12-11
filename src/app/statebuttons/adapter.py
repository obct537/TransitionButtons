from plone.app.users.browser.personalpreferences import PersonalPreferencesPanelAdapter
from app.statebuttons.userdataschema import IEnhancedUserDataSchema
from zope.interface import implements

class EnhancedUserDataPanelAdapter(PersonalPreferencesPanelAdapter):
    """
    """
    implements(IEnhancedUserDataSchema)

    def get_buttonDisabled(self):
        return self.context.getProperty('buttonsDisabled', '')
    def set_buttonsDisabled(self, value):
        return self.context.setMemberProperties({'buttonsDisabled': value})
    buttonsDisabled = property(get_buttonDisabled, set_buttonsDisabled)