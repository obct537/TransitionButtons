from  app.statebuttons.testing import APP_STATEBUTTONS_FUNCTIONAL_TESTING
from plone.testing import layered
import robotsuite
import unittest


def test_suite():
    suite = unittest.TestSuite()
    suite.addTests([
        layered(robotsuite.RobotTestSuite("robot_test.txt"),
                layer=APP_STATEBUTTONS_FUNCTIONAL_TESTING)
    ])
    return suite