from z3c.form import interfaces

from zope import schema
from zope.interface import Interface

from zope.i18nmessageid import MessageFactory

_ = MessageFactory('app.statebuttons')


class IButtonSettings(Interface):
    """Global akismet settings. This describes records stored in the
    configuration registry and obtainable via plone.registry.
    """

    button_name = schema.TextLine(title=_(u"Akismet (Wordpress) Key"),
                                  description=_(u"help_akismet_key",
                                                default=u"Enter in your Wordpress key here to "
                                                         "use Akismet to check for spam in comments."),
                                  required=False,
                                  default=u'',)

    pageElement = schema.TextLine(title=u'Site element.', default=u'#portalBreadcrumbs')
