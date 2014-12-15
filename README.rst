kotti_bootswatch_theme
**********************

bootswatch theme

|build status|_

`Find out more about Kotti`_

Development happens at https://github.com/mete0r/kotti_bootswatch_theme

.. |build status| image:: https://secure.travis-ci.org/mete0r/kotti_bootswatch_theme.png?branch=master
.. _build status: http://travis-ci.org/mete0r/kotti_bootswatch_theme
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    [app:kotti]

    ...

    kotti.configurators =
        kotti_bootswatch_theme.kotti_configure
    kotti_bootswatch_theme.theme = darkly

    ...

    [filter:fanstatic]
    use = egg:fanstatic#fanstatic
    rollup = True

    ...

Development
===========

Contributions to kotti_bootswatch_theme are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/mete0r/kotti_bootswatch_theme/issues
.. _Github repository: https://github.com/mete0r/kotti_bootswatch_theme
