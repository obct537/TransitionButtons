
from Products.CMFCore.utils import getToolByName

def uninstall(portal):
    profile = 'profile-app.statebuttons:uninstall'
    setup_tool = getToolByName(portal, 'portal_setup')
    setup_tool.runAllImportStepsFromProfile(profile)
    return "Ran all uninstall steps."