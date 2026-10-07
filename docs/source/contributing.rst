Contributing
============

Contributions of new templates, fixes and sample data are welcome via pull
requests to the
`GitHub repository <https://github.com/World-Meteorological-Organization/csv2bufr-templates>`_.

To report a correction, error or omission in a template, sample file or this
documentation, please
`raise an issue <https://github.com/World-Meteorological-Organization/csv2bufr-templates/issues>`_
on GitHub. Include the template name and version, and, where possible, the
input data and the BUFR message or error produced.

When adding a new template, please:

#. Add the template JSON to ``templates/``, conforming to
   ``csv2bufr-template-v2.json`` or ``csv2bufr-template-v4.json``, with a
   complete ``metadata`` block. Use v4 if the template needs features only
   available in that version, such as ``pack_subsets`` to encode multiple
   CSV rows as subsets of a single BUFR message.
#. Add an example CSV file to ``samples/``.
#. Add a page for the template under ``docs/source/templates/`` and list it in
   ``docs/source/templates/index.rst``.
#. Add the template to the contents list in ``README.md``.

Versions and provenance
-----------------------

Every change to a template that is published must be traceable, so that a
BUFR message, or an error found in one, can be linked back to the exact
mapping used to produce it. The ``metadata`` block of each template records
this:

``version``
   The template version. Increase it for every published change.

``id``
   A UUID that identifies this template **at this version**. Generate a new
   UUID (version 4) whenever the version changes; never reuse an ``id``.

``dateModified`` and ``editor``
   The date of the current version and the person who made it.

``references``
   The documents the template has been checked against, for example the
   relevant regulations in the *Manual on Codes* (WMO-No. 306) and the
   edition used. The BUFR master table version is given separately in the
   template's ``masterTablesVersionNumber``.

``history``
   One entry per version, oldest first, each with ``version``, ``id``,
   ``date``, ``editor`` and ``changes``, and optionally ``references`` to the
   regulations that motivated the change. The last entry must match the
   current ``version`` and ``id``.

For example:

.. code-block:: json

   {
       "metadata": {
           "label": "CLIMAT",
           "version": "1.1",
           "editor": "...",
           "dateModified": "2026-10-07",
           "id": "c802d3c6-fc95-443d-96db-41ff373a90b2",
           "references": [
               {
                   "title": "Manual on Codes (WMO-No. 306), Volume I.2",
                   "edition": "2023",
                   "section": "B/C30 - Regulations for reporting CLIMAT data in TDCF"
               }
           ],
           "history": [
               {"version": "1.0", "id": "99cad042-a73d-40a9-a646-cf140612394d",
                "date": "2025-07-09", "editor": "...", "changes": "Initial version."},
               {"version": "1.1", "id": "c802d3c6-fc95-443d-96db-41ff373a90b2",
                "date": "2026-10-07", "editor": "...",
                "changes": "Start of month fixed to day 1, 00:00.",
                "references": ["B/C30.1.1", "B/C30.2.1.2"]}
           ]
       }
   }

Update the version shown on the template's documentation page at the same
time.

Building the documentation locally
----------------------------------

.. code-block:: bash

   pip install -r docs/requirements.txt
   cd docs
   make html

The generated HTML is written to ``docs/_build/html``.
