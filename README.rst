kotti_bootswatch
****************

`Bootswatch`_ theme and theme generator for `Kotti`_.

This theme and the generated themes supersede css files of the `js.bootstrap`_
and Kotti via `fanstatic`_'s `supersedes`_ and `rollup`_ mechanism.

Development happens at https://github.com/mete0r/kotti_bootswatch

.. _Kotti: http://pypi.python.org/pypi/Kotti
.. _Bootswatch: http://bootswatch.com/
.. _js.bootstrap: https://pypi.python.org/pypi/js.bootstrap
.. _fanstatic: http://www.fanstatic.org
.. _supersedes: http://www.fanstatic.org/en/latest/api.html?highlight=supersedes#fanstatic.Resource
.. _rollup: http://www.fanstatic.org/en/latest/configuration.html#rollup


Basic usage: predefined bootswatch themes
=========================================

To enable the extension in your Kotti site, activate the configurator::

    [app:kotti]

    ...

    kotti.configurators =
        ...
        kotti_bootswatch.kotti_configure  # enable this extension

    # Use predefined `darkly' bootswatch theme
    kotti_bootswatch.theme = darkly  

    ...

    [filter:fanstatic]
    use = egg:fanstatic#fanstatic

    # fanstatic rollup should be enabled
    rollup = True

    ...


Advanced usage: generate and use a bootswatch-based themes
==========================================================

You can generate bootswatch-based themes::

    pcreate -s kotti_bootswatch mytheme
    cd mytheme
    sh quickstart.sh amelia  # use `amelia' bootswatch theme as a base theme

Read generated README.rst for more information::

    cat mytheme/README.rst


To use the generated theme in your Kotti site::

    [app:kotti]

    ...

    kotti.configurators =
        ...
        mytheme.kotti_configure  # enable this extension

    [filter:fanstatic]
    use = egg:fanstatic#fanstatic

    # fanstatic rollup should be enabled
    rollup = True


Caveat
======

Generated themes contains less files (`static/kotti/*.less`) to override Kotti
css files, i.e.  base/view/edit/upload.css. These less files are introduced to
adapt the Kotti css files to the bootstrap(or bootswatch) variables.

So if the original css files in the Kotti changes, the less files should be
changed too.


Development
===========

Contributions to kotti_bootswatch are highly welcome.
Just clone its `Github repository`_ and submit your contributions as pull requests.

.. _tracker: https://github.com/mete0r/kotti_bootswatch/issues
.. _Github repository: https://github.com/mete0r/kotti_bootswatch
