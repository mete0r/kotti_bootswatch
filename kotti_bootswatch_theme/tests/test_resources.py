# -*- coding: utf-8 -*-

"""
Created on 2014-12-03
:author: mete0r (mete0r@sarangbang.or.kr)
"""

from pytest import raises


def test_model(root, db_session):
    from kotti_bootswatch_theme.resources import CustomContent

    cc = CustomContent()
    assert cc.custom_attribute is None

    cc = CustomContent(custom_attribute=u'Foo')
    assert cc.custom_attribute == u'Foo'

    root['cc'] = cc = CustomContent()
    assert cc.name == 'cc'

    with raises(TypeError):
        cc = CustomContent(doesnotexist=u'Foo')
