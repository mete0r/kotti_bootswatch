# -*- coding: utf-8 -*-

"""
Created on 2014-12-03
:author: mete0r (mete0r@sarangbang.or.kr)
"""

from pyramid.i18n import TranslationStringFactory

_ = TranslationStringFactory('kotti_bootswatch_theme')


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_bootswatch_theme.kotti_configure

        to enable the ``kotti_bootswatch_theme`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """

    settings['pyramid.includes'] += ' kotti_bootswatch_theme'

    import os.path
    from .fanstatic_compiler import BOOTSTRAP_LESS_COMPILER
    theme = settings.get('kotti_bootswatch_theme.theme', 'custom')
    theme_dir = os.path.join(os.path.dirname(__file__), 'static', 'bootswatch',
                             theme)
    BOOTSTRAP_LESS_COMPILER.include_path = theme_dir
    view_resources = ' '.join([
        'kotti_bootswatch_theme.fanstatic.bootswatch_' + theme,
        'kotti_bootswatch_theme.fanstatic.kotti_override_base_css',
        'kotti_bootswatch_theme.fanstatic.kotti_override_view_css',
    ])
    edit_resources = ' '.join([
        'kotti_bootswatch_theme.fanstatic.bootswatch_' + theme,
        'kotti_bootswatch_theme.fanstatic.kotti_override_base_css',
        'kotti_bootswatch_theme.fanstatic.kotti_override_edit_css',
    ])
    settings['kotti.fanstatic.view_needed'] += ' ' + view_resources
    settings['kotti.fanstatic.edit_needed'] += ' ' + edit_resources


def includeme(config):
    """ Don't add this to your ``pyramid_includes``, but add the
    ``kotti_configure`` above to your ``kotti.configurators`` instead.

    :param config: Pyramid configurator object.
    :type config: :class:`pyramid.config.Configurator`
    """

    config.scan(__name__)
