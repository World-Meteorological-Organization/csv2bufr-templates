Overview
========

What is a csv2bufr template?
----------------------------

`csv2bufr <https://csv2bufr.readthedocs.io>`_ converts tabular (CSV) data to
WMO BUFR edition 4 messages. The conversion is driven by a JSON *mapping
template* that tells csv2bufr:

* how to read the CSV file (number of header rows, which row holds the column
  names, delimiter and quoting);
* which values to place in the BUFR header sections (data category,
  sub-category, master table version, typical date/time, etc.);
* the BUFR sequence to encode (``unexpandedDescriptors``);
* how each CSV column maps to an ecCodes key in the data section, including
  any scaling, offsets and valid ranges;
* replication factors for any delayed replication in the sequence.

The full template specification is described in the
`csv2bufr documentation <https://csv2bufr.readthedocs.io>`_.

Template structure
------------------

Each template declares the version of the csv2bufr template schema it
conforms to in ``conformsTo``. Most templates in this repository conform to
``csv2bufr-template-v2.json``. Newer templates, such as ``daycli-v3.json``,
conform to ``csv2bufr-template-v4.json``, which allows multiple CSV rows to be
encoded as subsets of a single BUFR message (``pack_subsets``). These require
a version of csv2bufr that supports the v4 schema.

The templates share the same top-level layout, shown here for a v2 template:

.. code-block:: json

   {
       "conformsTo": "csv2bufr-template-v2.json",
       "metadata": {
           "label": "...",
           "description": "...",
           "version": "...",
           "author": "...",
           "editor": "",
           "dateCreated": "YYYY-MM-DD",
           "dateModified": "YYYY-MM-DD",
           "id": "<uuid>"
       },
       "inputShortDelayedDescriptorReplicationFactor": [],
       "inputDelayedDescriptorReplicationFactor": [],
       "inputExtendedDelayedDescriptorReplicationFactor": [],
       "number_header_rows": 1,
       "column_names_row": 1,
       "quoting": "QUOTE_NONE",
       "header": [
           {"eccodes_key": "edition", "value": "const:4"}
       ],
       "data": [
           {"eccodes_key": "#1#airTemperature", "value": "data:air_temperature"}
       ]
   }

Values are given as ``const:<value>`` for fixed values, ``data:<column>`` for
values read from a CSV column, or ``array:<values>`` for lists (for example,
the BUFR sequence descriptors). The values in an array are separated by
commas, for example ``array:301150,307096`` or ``array:301150, 307096``.

Repository layout
-----------------

``templates/``
   The mapping templates (JSON).

``samples/``
   Example CSV files that can be used to test the templates.

``docs/``
   This documentation.

Available templates
-------------------

See :doc:`templates/index` for the list of templates and a summary of each.
