kotti_bootswatch
****************

bootswatch theme

|build status|_

`Find out more about Kotti`_

Development happens at https://github.com/mete0r/kotti_bootswatch

.. |build status| image:: https://secure.travis-ci.org/mete0r/kotti_bootswatch.png?branch=master
.. _build status: http://travis-ci.org/mete0r/kotti_bootswatch
.. _Find out more about Kotti: http://pypi.python.org/pypi/Kotti

Setup
=====

To enable the extension in your Kotti site, activate the configurator::

    [app:kotti]

    ...

    kotti.configurators =
        kotti_bootswatch.kotti_configure
    kotti_bootswatch.theme = darkly

    ...

    [filter:fanstatic]
    use = egg:fanstatic#fanstatic
    rollup = True

    ...

Development
===========

Contributions to kotti_bootswatch are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/mete0r/kotti_bootswatch/issues
.. _Github repository: https://github.com/mete0r/kotti_bootswatch
