# -*- coding: utf-8 -*-

"""
Created on 2014-12-03
:author: mete0r (mete0r@sarangbang.or.kr)
"""

from pytest import fixture


@fixture
def dummy_content(root):

    from kotti_bootswatch_theme.resources import CustomContent

    root['cc'] = cc = CustomContent(
        title=u'My content',
        description=u'My very custom content is custom',
        custom_attribute='Lorem ipsum'
    )

    return cc


def test_view(dummy_content, dummy_request):

    from kotti_bootswatch_theme.views.view import CustomContentViews

    views = CustomContentViews(dummy_content, dummy_request)

    default = views.default_view()
    assert 'foo' in default

    alternative = views.alternative_view()
    assert alternative['foo'] == u'bar'
