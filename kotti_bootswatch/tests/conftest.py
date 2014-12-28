# -*- coding: utf-8 -*-

"""
Created on 2014-12-03
:author: mete0r (mete0r@sarangbang.or.kr)
"""

pytest_plugins = "kotti"

from pytest import fixture


@fixture(scope='session')
def custom_settings():
    return {
        'kotti.configurators': 'kotti_tinymce.kotti_configure '
                               'kotti_bootswatch.kotti_configure'}
