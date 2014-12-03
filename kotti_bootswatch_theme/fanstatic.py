# -*- coding: utf-8 -*-

"""
Created on 2014-12-03
:author: mete0r (mete0r@sarangbang.or.kr)
"""

from __future__ import absolute_import

from fanstatic import Group
from fanstatic import Library
from fanstatic import Resource

from js.bootstrap import bootstrap_css

from kotti.fanstatic import base_css as kotti_base_css
from kotti.fanstatic import view_css as kotti_view_css
from kotti.fanstatic import edit_css as kotti_edit_css
from kotti.fanstatic import upload_css as kotti_upload_css


library = Library("kotti_bootswatch_theme", "static")

bootswatch_names = ['amelia', 'cerulean', 'cosmo', 'cyborg', 'darkly',
                    'flatly', 'journal', 'lumen', 'paper', 'readable',
                    'sandstone', 'simplex', 'slate', 'spacelab',
                    'superhero', 'united', 'yeti']
bootswatch_resources = dict((name,
                             Resource(library,
                                      'bootswatch/' + name + '/bootstrap.css',
                                      supersedes=[bootstrap_css]))
                            for name in bootswatch_names)
for name in bootswatch_resources:
    globals()['bootswatch_' + name] = bootswatch_resources[name]
del name

kotti_override_base_css = Resource(library, 'kotti_override/base.css',
                                   source='kotti_override/base.less',
                                   compiler='bootstrapless',
                                   depends=[kotti_base_css])
kotti_override_view_css = Resource(library, 'kotti_override/view.css',
                                   source='kotti_override/view.less',
                                   compiler='bootstrapless',
                                   depends=[kotti_view_css,
                                            kotti_override_base_css])
kotti_override_edit_css = Resource(library, 'kotti_override/edit.css',
                                   source='kotti_override/edit.less',
                                   compiler='bootstrapless',
                                   depends=[kotti_edit_css,
                                            kotti_override_base_css])
kotti_override_upload_css = Resource(library, 'kotti_override/upload.css',
                                     source='kotti_override/upload.less',
                                     compiler='bootstrapless',
                                     depends=[kotti_upload_css,
                                              kotti_override_base_css])
kotti_override_css = Group([
    kotti_override_base_css,
    kotti_override_view_css,
    kotti_override_edit_css,
    kotti_override_upload_css,
])
