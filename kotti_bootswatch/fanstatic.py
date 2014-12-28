# -*- coding: utf-8 -*-

"""
Created on 2014-12-03
:author: mete0r (mete0r@sarangbang.or.kr)
"""

from __future__ import absolute_import

from fanstatic import Library
from fanstatic import Resource

from js.bootstrap import bootstrap_css

from kotti.fanstatic import base_css as kotti_base_css
from kotti.fanstatic import view_css as kotti_view_css
from kotti.fanstatic import edit_css as kotti_edit_css
from kotti.fanstatic import upload_css as kotti_upload_css


library = Library("kotti_bootswatch", "static")


def supersede_resources(theme):
    theme = str(theme)

    bootstrap_path = 'bootswatch/' + theme + '/bootstrap.css'
    Resource(library, bootstrap_path, supersedes=[bootstrap_css])

    basepath = 'kotti/' + theme + '/'
    Resource(library, basepath + 'base.css', supersedes=[kotti_base_css])
    Resource(library, basepath + 'view.css', supersedes=[kotti_view_css])
    Resource(library, basepath + 'edit.css', supersedes=[kotti_edit_css])
    Resource(library, basepath + 'upload.css', supersedes=[kotti_upload_css])
