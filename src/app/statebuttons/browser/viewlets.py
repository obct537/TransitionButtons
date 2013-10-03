from Products.Five.browser.pagetemplatefile import ViewPageTemplateFile
from plone.app.layout.viewlets.common import ViewletBase
from Products.CMFCore.utils import getToolByName
from app.statebuttons.interfaces import IButtonSettings

from zope.component import queryUtility
from plone.registry.interfaces import IRegistry
from string import split
import json

class ButtonViewlet(ViewletBase):
    render = ViewPageTemplateFile('js_viewlet.pt')
    settings = [];

    def getSettings(self):
        registry = queryUtility(IRegistry)
        settings = registry.forInterface(IButtonSettings, False)
        return settings

    def getStates(self):

        stateList = [];

        wf_tool = getToolByName(self, 'portal_workflow')
        defaultWorkflow = wf_tool.getChainForPortalType(self.context)

        states = wf_tool[ defaultWorkflow[0] ].states

        if states:

            for state in states:
                stateList.append(state)

            return stateList
        else:
            return False

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

            return json.dumps(transitionList, sort_keys=False)
        else:
            return False
        
    def update(self):

        #import pdb; pdb.set_trace()

        settings = self.getSettings()

        self.js_info = self.getTransitions
        self.wf_state = self.getWFState
        self.pageElement = settings.pageElement
        self.workflowDescription = self.getStateDescription


