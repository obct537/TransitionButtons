
from plone.app.users.browser.personalpreferences import IPersonalPreferences
from zope.interface import Interface
from zope import schema


class IEnhancedUserDataSchema(IPersonalPreferences):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """

    buttonsEnabled = schema.Bool(title=u'Transition button widget.', 
                                default=True,
                                description=u'Uncheck to remove the transition button box from ALL pages.',
                                required=False
                                )