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
    minified_path = 'bootswatch/' + theme + '/bootstrap.min.css'
    Resource(library, bootstrap_path, minified=minified_path,
             supersedes=[bootstrap_css])

    basepath = 'kotti/' + theme + '/'
    resource_map = {
        'base': kotti_base_css,
        'view': kotti_view_css,
        'edit': kotti_edit_css,
        'upload': kotti_upload_css
    }
    for key, kotti_css in resource_map.items():
        Resource(library, basepath + key + '.css',
                 minified=basepath + key + '.min.css',
                 supersedes=[kotti_css])
