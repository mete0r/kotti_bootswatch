# -*- coding: utf-8 -*-

"""
Created on 2014-12-03
:author: mete0r (mete0r@sarangbang.or.kr)
"""

bootswatch_names = ['amelia', 'cerulean', 'cosmo', 'cyborg', 'darkly',
                    'flatly', 'journal', 'lumen', 'paper', 'readable',
                    'sandstone', 'simplex', 'slate', 'spacelab',
                    'superhero', 'united', 'yeti']


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_bootswatch.kotti_configure

        to enable the ``kotti_bootswatch`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """
    from .fanstatic import supersede_resources

    theme = settings.get('kotti_bootswatch.theme', 'custom')
    supersede_resources(theme)
