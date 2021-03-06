Documentation
=============

:name:          taptaptap
:author:        Lukas Prokop
:date:          Feb-Apr 2014, Jul 2018
:license:       BSD 3-clause
:version:       1.2.1
:issues:        http://github.com/meisterluk/taptaptap/issues

Test Anything Protocol handling for cats \*rawwr*

.. contents:: Table of contents

``taptaptap`` provides parsers, writers and APIs to handle the Test Anything Protocol (TAP). The implementation focuses on the most-current TAP version 13. TAP originates from the Perl community, but is a general format to document runs of testsuites. The reference to cats is just a pun for the noise of cats sneaking on floors.

Compatibility
-------------

``taptaptap`` is only supposed to be working with python 2.7 (due to with statements and argparse).
It fully supports unicode.
It has been tested with Xubuntu 18.04 (Linux 4.15 x86_64) on 2.7.15rc1. A version for python 3.x is available as package ``taptaptap3``.

Changelog
---------
:1.2.1: declare encoding in setup.py, README updates
:1.2.0: Bugfix: do not drop memo in TapBailout,
        shebangs: "python" → "python2",
        Bugfix: initialize next_number with 1,
        Bugfix: issue #1
:1.1.3: tapmerge: support merging more than 2 TAP files,
        support "-" to denote stdin
:1.1.2: TapWriter: do not reuse TapWriter instance in TapCreator
:1.1.1: TapWriter: support data handling in TapBailout
:1.1.0: procedural API writes to stderr not stdout,
        bugfix TapCreator: Fix number of testcase determination
:1.0.5: bugfix procedural API: write version even if default version
:1.0.4: more tests, fix output/source bug in testsuite
:1.0.3: install_requires in setup.py
:1.0.2: introduce requirements.txt
:1.0.1: Unicode improvements
:1.0.0: First stable release, packaging improvements, full testsuite
:0.8.0: Unstable release, minimal testsuite

The File Format
---------------

A basic introduction is given by Wikipedia. The format was specified by the Perl community.

* `The Wikipedia article <https://en.wikipedia.org/wiki/Test_Anything_Protocol>`_
* `Original specification <http://web.archive.org/web/20120730055134/http://testanything.org/wiki/index.php/TAP_specification>`_
* `Test::Harness <https://metacpan.org/pod/release/PETDANCE/Test-Harness-2.64/lib/Test/Harness/TAP.pod#THE-TAP-FORMAT>`_

Testsuite & Examples
--------------------

``taptaptap`` comes with a testsuite, which covers many special cases of the TAP format and tests the provided APIs. Please don't hesitate to report any issues_.

You can run the ``taptaptap`` testcases yourself using::

    ./run.sh

in the tests directory. The testsuite also shows some API usage examples, but I want to provide some here. The procedural API is well-suited if you are in the python REPL::

    from taptaptap.proc import plan, ok, not_ok, out
    plan(tests=10)
    ok('Starting the robot')
    not_ok('Starting the engine')
    not_ok('Find the object', skip='Setup required')
    not_ok('Terminate', skip='Setup required')

    out()

The output looks like this::

    1..10
    ok - Starting the robot
    not ok - Starting the engine
    not ok - Find the object  # SKIP Setup required
    not ok - Terminate  # SKIP Setup required

Be aware that the state is stored within the module. This is not what you want if you are outside the REPL. The ``TapWriter`` class is more convenient in this case::

    import taptaptap

    writer = taptaptap.TapWriter()
    writer.plan(1, 3)
    writer.ok('This testcase went fine')
    writer.ok('And another one')
    writer.ok('And also the last one')

If you like python's generators, you want to use ``SimpleTapCreator``::

    @taptaptap.SimpleTapCreator
    def runTests():
        yield True
        yield True
        yield False

    print runTests()

Giving us::

    1..3
    ok
    ok
    not ok

Or take a look at the more sophisticated ``TapCreator``. If you are a real expert, you can use ``TapDocument`` directly, which covers all possibilities of TAP.

Command line tools
------------------

You can also invoke ``taptaptap`` directly from the command line::

    python -m taptaptap.__main__ some_tap_file_to_validate.tap

This command will parse the file and write the file in a way how it was understood by the module. The exit code indicates its validity:

0
  Everything fine.
1
  The TAP file is missing some testcases or contains failed testcases.
2
  A bailout was raised. So the testing environment crashed during the run.

Pickling
--------

All objects are pickable.

When to use ``taptaptap``
-------------------------

Does ``taptaptap`` suite your needs?
It does, if you are looking for a parser and validator for your TAP documents and you don't want to care about details and just need a gentle API.

best regards,
meisterluk

.. _issues: https://github.com/meisterluk/taptaptap
