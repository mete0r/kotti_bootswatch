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

from . import bootswatch_names


library = Library("kotti_bootswatch_theme", "static")

bootswatch_resources = dict((name,
                             Resource(library,
                                      'bootswatch/' + name + '/bootstrap.css',
                                      supersedes=[bootstrap_css]))
                            for name in bootswatch_names)


def resources_callback(name):
    globals()['bootswatch_' + name] = bootswatch_resources[name]
map(resources_callback, bootswatch_names)


def overrides_callback(name):
    d = globals()

    basepath = 'kotti_override/' + name + '/'

    kotti_override_base_css = Resource(library, basepath + 'base.css',
                                       depends=[kotti_base_css])
    kotti_override_view_css = Resource(library, basepath + 'view.css',
                                       depends=[kotti_view_css,
                                                kotti_override_base_css])
    kotti_override_edit_css = Resource(library, basepath + 'edit.css',
                                       depends=[kotti_edit_css,
                                                kotti_override_base_css])
    kotti_override_upload_css = Resource(library, basepath + 'upload.css',
                                         depends=[kotti_upload_css,
                                                  kotti_override_base_css])
    kotti_override_css = Group([
        kotti_override_base_css,
        kotti_override_view_css,
        kotti_override_edit_css,
        kotti_override_upload_css,
    ])

    override_prefix = 'kotti_override_bootswatch_'
    prefixed_name = override_prefix + name
    d[prefixed_name + '_base_css'] = kotti_override_base_css
    d[prefixed_name + '_view_css'] = kotti_override_view_css
    d[prefixed_name + '_edit_css'] = kotti_override_edit_css
    d[prefixed_name + '_upload_css'] = kotti_override_upload_css
    d[prefixed_name + '_css'] = kotti_override_css
map(overrides_callback, bootswatch_names)
