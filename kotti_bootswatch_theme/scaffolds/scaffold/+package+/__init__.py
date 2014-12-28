# -*- coding: utf-8 -*-

"""
"""


def kotti_configure(settings):
    """ Add a line like this to you .ini file::

            kotti.configurators =
                kotti_bootswatch_theme.kotti_configure

        to enable the ``kotti_bootswatch_theme`` add-on.

    :param settings: Kotti configuration dictionary.
    :type settings: dict
    """
    from .fanstatic import supersede_resources

    supersede_resources()
