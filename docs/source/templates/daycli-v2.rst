daycli-template (deprecated)
============================

:Status: **Deprecated**, replaced by :doc:`daycli` (307095)
:Template: :template:`daycli-template.json`
:DAYCLI version: 2
:Template version: 3
:BUFR sequence: ``307075``
:Data category / sub-category: 0 / 21
:Template schema: ``csv2bufr-template-v2.json``
:Header rows: 1 (column names in row 1)
:Sample data: :sample:`daycli.csv`

Template for version 2 of the DAYCLI data format (BUFR sequence 307075).
Each row in the CSV file is encoded as a separate BUFR message containing a
single subset.

.. warning::

   **Deprecated.** DAYCLI version 2 (sequence 307075) has been replaced by
   version 3 (sequence 307095). This template is kept for users who still
   exchange DAYCLI data using sequence 307075. New implementations should
   use :doc:`daycli`.

Background
----------

DAYCLI is used to exchange nationally validated daily climate values from
surface land stations. Each row contains six variables for a single station
and day:

* Daily maximum, minimum and mean air temperature
* Daily total accumulated precipitation
* Daily depth of fresh snow
* Total snow depth

Differences from version 3
^^^^^^^^^^^^^^^^^^^^^^^^^^

Version 2 records a single date for the row and, for each variable, a day
offset and a time of day. It does not include an offset from UTC or an
explicit end time for each period. Version 3 (307095) replaced this with an
explicit start and end time for each period, an Attribution day and the
difference between the local meteorological time zone and UTC, to remove
ambiguity in the period each value covers. The discussion is at
https://github.com/wmo-im/BUFR4/issues/238.

Observation periods and times
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``year``, ``month`` and ``day`` columns give the date the row's values
are assigned to. They are also used for the date in the BUFR header (section
1), with the time in the header set to 23:59.

For each variable, the period over which the value was calculated is given
relative to this date by four columns:

* ``*_day_offset``: the time period or displacement, in days (0 04 023),
  ``0`` for the same day as ``day`` or ``-1`` for the day before.
* ``*_hour``, ``*_minute`` and ``*_second``: the time of day.

Together these give the start of the 24 hour period over which the
statistic was calculated. In the sample data, for example, precipitation
and maximum temperature have ``0``, ``7``, ``0``, ``1``, a period starting
at 07:00:01 on the day and ending at 07:00:00 the following day, and mean
temperature has ``0``, ``0``, ``0``, ``1``, the calendar day. For total snow
depth, which is a spot measurement, the columns give the time of the
measurement. The periods selected should match national reporting practices
for each variable.

Quality flags
^^^^^^^^^^^^^

Each variable has a ``*_flag`` column, encoded as an associated field with
significance 5 (8 bit indicator of quality control class). The template
accepts values 0 - 7, with the same meanings as the quality flags used in
DAYCLI version 3, see :ref:`quality flags <quality-flags>`.

Station metadata
^^^^^^^^^^^^^^^^

``temperature_siting_classification`` and
``precipitation_siting_classification`` use BUFR code tables 0 08 095 and
0 08 096, and ``averaging_method`` uses BUFR code table 0 08 094. These are
the same code tables as in DAYCLI version 3, see
:ref:`siting and measurement quality classification <siting-codes>` and
:ref:`method used to calculate the average daily temperature <method-codes>`.

Input CSV
---------

.. note::

   The CSV format described here is defined for this csv2bufr template only.
   It is not a WMO standard. The column names and layout are a convenience
   for preparing data for conversion; the standard is the BUFR sequence
   307075 defined in the *Manual on Codes* (WMO-No. 306), Volume I.2.

File format
^^^^^^^^^^^

* Comma separated (``,``), with no quoting of values.
* One header row containing the column names. Columns are matched by name,
  so their order does not matter, but every column listed below must be
  present.
* One row per station per day. Each row becomes one BUFR message.
* An empty cell is encoded as missing. Values that are not measured, not
  available or not known should be left empty rather than filled with a
  placeholder such as ``-999``.
* Values must be in the units shown. In particular, temperatures are in
  kelvin (K = °C + 273.15) and snow depths are in metres.
* Temperatures must be given in kelvin to 2 decimal places. A value in °C to
  1 decimal place has 2 decimal places once converted (23.4 °C = 296.55 K).
  Rounding it to 1 decimal place in kelvin (296.6 K) changes the value,
  which then decodes as 23.5 °C.

Station identification and metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These columns normally repeat on every row for a station. The WIGOS
identifier, ``0-20000-0-72565`` for example, is split across the four
``wsi_*`` columns.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``wsi_series``
     - WIGOS identifier series (first block of the WSI)
     - 0
   * - ``wsi_issuer``
     - WIGOS issuer of identifier (second block), e.g. 20000
     - 0 - 65534
   * - ``wsi_issue_number``
     - WIGOS issue number (third block)
     - 0 - 65534
   * - ``wsi_local``
     - WIGOS local identifier (fourth block), e.g. 72565
     - text, up to 16 characters
   * - ``wmo_block_number``
     - Traditional WMO block number (first two digits of the five-digit station index). Leave empty if the station has none.
     - 0 - 99
   * - ``wmo_station_number``
     - Traditional WMO station number (last three digits of the station index). Leave empty if the station has none.
     - 0 - 999
   * - ``latitude``
     - Station latitude (WGS-84), north positive
     - degrees, -90 - 90
   * - ``longitude``
     - Station longitude (WGS-84), east positive
     - degrees, -180 - 180
   * - ``station_height_above_msl``
     - Height of the station ground above mean sea level
     - m, -400 - 9000
   * - ``thermometer_height``
     - Height of the temperature sensor above local ground
     - m, 2 decimal places
   * - ``temperature_siting_classification``
     - Combined siting and measurement quality classification of the temperature sensor
     - BUFR code table 0 08 095
   * - ``precipitation_siting_classification``
     - Combined siting and measurement quality classification of the precipitation gauge
     - BUFR code table 0 08 096
   * - ``averaging_method``
     - Method used to calculate the daily mean temperature
     - BUFR code table 0 08 094

Date
^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year``
     - Year the values are assigned to
     - 1800 - 2100
   * - ``month``
     - Month the values are assigned to
     - 1 - 12
   * - ``day``
     - Day the values are assigned to
     - 1 - 31

Observed variables
^^^^^^^^^^^^^^^^^^

Each variable uses the same set of columns, with the prefix shown in the
table below. For example, the precipitation columns are
``precipitation_day_offset``, ``precipitation_hour``,
``precipitation_minute``, ``precipitation_second``, ``precipitation`` and
``precipitation_flag``.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``<prefix>_day_offset``
     - Day of the start of the period (or of the measurement, for total snow depth), relative to ``day``
     - days, -1 or 0
   * - ``<prefix>_hour``
     - Hour of the start of the period (or of the measurement)
     - 0 - 23
   * - ``<prefix>_minute``
     - Minute of the start of the period (or of the measurement)
     - 0 - 59
   * - ``<prefix>_second``
     - Second of the start of the period (or of the measurement)
     - 0 - 59
   * - ``<value column>``
     - The value, see below
     -
   * - ``<value column>_flag``
     - Quality flag for the value
     - 0 - 7, see `Quality flags`_

.. list-table::
   :header-rows: 1
   :widths: 25 25 30 20

   * - Variable
     - Prefix
     - Value column
     - Units / values
   * - Total accumulated precipitation
     - ``precipitation``
     - ``precipitation``
     - kg m-2 (1 kg m-2 = 1 mm), 0 - 2000
   * - Depth of fresh snow
     - ``fresh_snow``
     - ``fresh_snow_depth``
     - m
   * - Total snow depth
     - ``total_snow``
     - ``total_snow_depth``
     - m
   * - Maximum air temperature
     - ``maximum_temperature``
     - ``maximum_temperature``
     - K, 2 decimal places, 183.15 - 343.15
   * - Minimum air temperature
     - ``minimum_temperature``
     - ``minimum_temperature``
     - K, 2 decimal places, 183.15 - 343.15
   * - Mean air temperature
     - ``average_temperature``
     - ``average_temperature``
     - K, 2 decimal places, 183.15 - 343.15

The first-order statistic for each temperature (maximum, minimum or mean)
is set by the template and is not read from the CSV file.
