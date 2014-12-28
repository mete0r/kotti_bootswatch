kotti_bootswatch
****************

bootswatch theme

`Find out more about Kotti`_

Development happens at https://github.com/mete0r/kotti_bootswatch

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


Theme generator
===============

You can generate bootswatch-based themes::

    pcreate -s kotti_bootswatch mytheme
    cd mytheme
    sh quickstart.sh amelia

Read generated README.rst for more information::

    cat mytheme/README.rst


Development
===========

Contributions to kotti_bootswatch are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/mete0r/kotti_bootswatch/issues
.. _Github repository: https://github.com/mete0r/kotti_bootswatch
