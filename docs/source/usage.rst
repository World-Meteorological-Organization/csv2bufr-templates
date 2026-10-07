Using the templates
===================

The templates are used with `csv2bufr <https://csv2bufr.readthedocs.io>`_.
Refer to the csv2bufr documentation for installation instructions and the
full command line and Python API reference.

Installing the templates
------------------------

Clone this repository and point csv2bufr at the ``templates`` directory using
the ``CSV2BUFR_TEMPLATES`` environment variable:

.. code-block:: bash

   git clone https://github.com/World-Meteorological-Organization/csv2bufr-templates.git
   export CSV2BUFR_TEMPLATES=$(pwd)/csv2bufr-templates/templates

Converting a file
-----------------

Convert one of the sample CSV files using the matching template:

.. code-block:: bash

   csv2bufr data transform samples/daycli.csv \
       --bufr-template daycli-template \
       --output-dir ./output

.. todo: confirm CLI options against the current csv2bufr release and add a
   Python API example.

Adapting a template
-------------------

If your CSV file does not match one of the templates exactly, copy the closest
template and edit the column names in the ``data:<column>`` references to
match your file. Remember to update the ``metadata`` block (``label``,
``description``, ``version``, ``author``, ``dateModified`` and a new ``id``).
