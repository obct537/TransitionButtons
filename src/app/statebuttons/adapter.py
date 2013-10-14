from plone.app.users.browser.personalpreferences import UserDataPanelAdapter

class EnhancedUserDataPanelAdapter(UserDataPanelAdapter):
    """
    """
    def get_buttonEnabled(self):
        return self.context.getProperty('buttonsEnabled', '')
    def set_buttonsEnabled(self, value):
        return self.context.setMemberProperties({'buttonsEnabled': value})
    buttonsEnabled = property(get_buttonEnabled, set_buttonsEnabled)