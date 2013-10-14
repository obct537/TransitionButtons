from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('app.statebuttons')


class IButtonSettings(Interface):
    """Global settings for the transition button panel. Settings stored in the 
       Plone registry
    """

    pageElement = schema.TextLine(title=u'Site element.', 
                                  default=u'#portal-breadcrumbs',
                                  description=u'Enter a CSS selector to attach the button box to.',
                                  required=False,)
