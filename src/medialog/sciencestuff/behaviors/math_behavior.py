# -*- coding: utf-8 -*-

from medialog.sciencestuff import _
from plone import schema
from plone.autoform.interfaces import IFormFieldProvider
from plone.dexterity.interfaces import IDexterityContent
from plone.supermodel import model
from zope.component import adapter
from zope.interface import Interface
from zope.interface import implementer
from zope.interface import provider


class IMathBehaviorMarker(Interface):
    pass

@provider(IFormFieldProvider)
class IMathBehavior(model.Schema):
    """
    """

    #project = schema.TextLine(
    #    title=_(u'Project'),
    #    description=_(u'Give in a project name'),
    #    required=False,
    #)


@implementer(IMathBehavior)
@adapter(IMathBehaviorMarker)
class MathBehavior(object):
    def __init__(self, context):
        self.context = context

    #@property
    #def project(self):
    #    if hasattr(self.context, 'project'):
    #        return self.context.project
    #    return None

    #@project.setter
    #def project(self, value):
    #    self.context.project = value
