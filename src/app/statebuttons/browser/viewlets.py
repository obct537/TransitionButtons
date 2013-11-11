from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from app.statebuttons.interfaces import IButtonSettings

from AccessControl.PermissionRole import rolesForPermissionOn

from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from string import split
import json

class ButtonViewlet(ViewletBase):
    render = ViewPageTemplateFile('js_viewlet.pt')
    settings = []

    def isPanelEnabled(self):

        memTool = getToolByName(self, 'portal_membership')
        user = memTool.getAuthenticatedMember()
        res = user.getProperty('buttonsEnabled')

        if( res == False or res == True ):
            return res
        else:
            #If the setting isn't set yet, it returns an object instead of true/false
            return False


    # gets the settings from the add-on control panel
    def getSettings(self):
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IButtonSettings, False)
        return settings

    def getWFState(self):
        wf_tool = getToolByName(self, 'portal_workflow')

        try:
            state = wf_tool.getInfoFor(self.context, 'review_state')
            return state
        except:
            return False

    def getStateDescription(self):

        wf_tool = getToolByName(self, 'portal_workflow')
        defaultWorkflow = wf_tool.getChainForPortalType(self.context.portal_type)

        state = self.getWFState()

        if not wf_tool:
            return False

        if not defaultWorkflow:
            return False

        try:
            # defaultWorkflow is a tuple, so we need to take the index of it
            # 
            # TODO: fix for sites with multiple simultaneous workflows?
            desc = wf_tool[ defaultWorkflow[0] ].states[state].description
        except:
            return False

        return desc

    def getTransitions(self):

        wf_tool = getToolByName(self, 'portal_workflow')
        defaultWorkflow = wf_tool.getChainForPortalType(self.context)

        transitions = wf_tool[ defaultWorkflow[0] ].transitions
        transitionList = [];

        if transitions:
            for transition in transitions:
                transitionList.append(transition)

            return transitionList
        else:
            return False

    def getRolesWithPermission(self):
        pUrl = getToolByName(self, 'portal_url')
        portal = pUrl.getPortalObject()
        roles = rolesForPermissionOn('View', self.context)
        memTool = getToolByName(self.context, 'portal_membership')

        members = memTool.listMembers()
        allowedMembers = []

        for mem in members:
            for role in roles:
                if( mem.has_role(role) == 1 ):

                    # If member's fullname isn't set, use their ID
                    name = mem.getProperty('fullname')
                    if( name != "" ):
                        allowedMembers.append(name)
                    else:
                        allowedMembers.append( mem.getProperty('id') )
                    # We don't need to check this user again.
                    break

        memberList = json.dumps(allowedMembers, sort_keys=False)

        return roles

    def setJson(self):

        panelSettings = self.getSettings()

        settings = {}
        settings["isPanelEnabled"] = self.isPanelEnabled()
        settings["allowedTransitions"] = self.getTransitions()
        settings["wfState"] = self.getWFState() 
        settings["stateDescription"] = self.getStateDescription()
        settings["pageElement"] = panelSettings.pageElement
        settings["floating"] = panelSettings.floating

        if( panelSettings.enableSharing ):
            settings["rolesWithPermission"] = self.getRolesWithPermission()

        return json.dumps(settings, sort_keys=False)

    def update(self):

        # if the user has disabled the panel, don't
        # bother with the rest of this stuff
        if( not self.isPanelEnabled() ):
            return 0

        self.buttonJson = self.setJson()

