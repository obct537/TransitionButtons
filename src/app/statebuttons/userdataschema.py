from plone.app.users.userdataschema import IUserDataSchemaProvider
from plone.app.users.userdataschema import IUserDataSchema
from zope.interface import Interface, implements
from zope import schema


class UserDataSchemaProvider(object):
    implements(IUserDataSchemaProvider)

    def getSchema(self):
        """
        """
        return IEnhancedUserDataSchema


class IEnhancedUserDataSchema(IUserDataSchema):
    """ Use all the fields from the default user data schema, and add various
    extra fields.
    """

    buttonsEnabled = schema.Bool(title=u'Transition buttons', 
                                default=True,
                                description=u'Uncheck to remove the transition button box from ALL pages.',
                                )