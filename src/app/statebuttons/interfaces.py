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

    enableSharing = schema.Bool(title=u'Enable sharing info.',
    							description=u'Choose whether or not to include page sharing information. </ br>' + 
    							"Enabling thing can cause performance issues on sites with a lot of members.",
    							required=False,)
    fixed = schema.Bool(title=u'Floating button box.',
                        description=u'Enable this option to make the transition button box float statically above the page',
                        required=False,
                        default=False)