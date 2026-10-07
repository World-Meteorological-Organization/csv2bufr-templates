daycli-template
===============

:Template: :template:`daycli-v3.json`
:Version: 3
:BUFR sequence: ``307095``
:Data category / sub-category: 0 / 21
:Template schema: ``csv2bufr-template-v4.json``
:Header rows: 1 (column names in row 1)
:Sample data: :sample:`daycli-v3.csv`

Template for version 3 of the DAYCLI data format (BUFR sequence 307095).
The template sets ``"pack_subsets": true``, so all rows in the CSV file are
encoded as subsets of a single BUFR message, rather than one message per
row. This requires a version of csv2bufr that supports the
``csv2bufr-template-v4.json`` schema.

Background
----------

DAYCLI is used to exchange nationally validated daily climate values from surface land stations, with the data exchanged
monthly after quality control. Each day is encoded as a separate subset, with each subset containing six variables from
a single station:

* Daily maximum, minimum and mean air temperature
* Daily total accumulated precipitation
* Daily depth of fresh snow
* Total snow depth at time of measurement

To more clearly define the period over which the daily statistics have been calculated, and to align with national
reporting practices, each statistic (min, max, mean, total/sum) has an explicit start and end time defined and encoded
using the local meteorological time zone (LMTZ). The offset between LMTZ and UTC is also included in the encoded data
to enable conversion to UTC. Noting that the 24 hour periods over which the statistics are calculated can span different
days, the BUFR sequence includes an explicit attribution day to which the statistics have been assigned. A full
discussion of the sequence development can be found at https://github.com/wmo-im/BUFR4/issues/238.

Attribution day and LMTZ
^^^^^^^^^^^^^^^^^^^^^^^^

The *Attribution day* is the calendar date, in LMTZ, that the NMHS assigns a daily value to. It is given by the
``attribution_year``, ``attribution_month`` and ``attribution_day`` columns in the CSV file. The difference between
the local meteorological time zone and UTC is given by the ``utc_offset`` column in minutes (LMTZ-UTC).
The LMTZ applies individually to each stations, noting countries can span multiple time zones.

Observation periods and times
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

Each daily, or 24 hour period, statistic is reported with the start and end time of the period over which it it was
calculated, in LMTZ, using the ``*_start`` and ``*_end`` columns. Total snow depth is an instantaneous value and
reported with a single measurement time (``*_total_snow_depth``). The periods selected should match national reporting
practices for each variable.

For example, for a station at UTC-4 with an Attribution day of 15 January
2026, the periods might be:

.. list-table::
   :header-rows: 1
   :widths: 40 30 30

   * - Variable
     - Start (LMTZ)
     - End (LMTZ)
   * - Total snow depth
     - 2026-01-15 08:00
     - (spot measurement)
   * - Precipitation
     - 2026-01-15 08:01
     - 2026-01-16 08:00
   * - Fresh snow
     - 2026-01-15 08:01
     - 2026-01-16 08:00
   * - Maximum temperature
     - 2026-01-15 08:01
     - 2026-01-16 08:00
   * - Minimum temperature
     - 2026-01-14 08:01
     - 2026-01-15 08:00
   * - Mean temperature
     - 2026-01-15 00:01
     - 2026-01-16 00:00

For this row, ``utc_offset`` is ``-240`` and ``attribution_year``,
``attribution_month`` and ``attribution_day`` are ``2026``, ``1`` and ``15``.

.. _quality-flags:

Quality flags
^^^^^^^^^^^^^

The quality flags included in the BUFR sequence for each variable indicate
whether the value has been checked and, if so, whether it is believed to be
good or suspect. They also indicate other potential issues, for example values
that have been aggregated, are out of instrument range or are missing. In the
CSV file, each variable has a ``*_quality`` column containing a flag from BUFR
code table 0 31 021.

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Flag
     - Meaning
   * - 0
     - Data checked and declared good
   * - 1
     - Data checked and declared suspect
   * - 2
     - Data checked and declared aggregated
   * - 3
     - Data checked and declared out of instrument range
   * - 4
     - Data checked, declared aggregated, and out of instrument range
   * - 5
     - Parameter is not measured at the station
   * - 6
     - Daily value not provided
   * - 7
     - Data unchecked
   * - 8 - 254
     - Reserved
   * - 255
     - Missing (QC information not available)

A value is *aggregated* when it covers more than one daily period. This
happens, for example, when a rain gauge or snow board is not read every day,
so the reported total includes precipitation from earlier days. It also
applies to a maximum or minimum temperature taken from a thermometer that was
not reset daily, where the extreme may have occurred on an earlier day.

Station metadata
^^^^^^^^^^^^^^^^

The BUFR sequence includes fields to record the exposure and quality of the
sensors used to measure temperature and precipitation, and the method used to
calculate the daily mean temperature.

.. _siting-codes:

**Siting and measurement quality classification**

The exposure and quality of the sensors are recorded using two complementary
classifications defined in the *Guide to Instruments and Methods of
Observation* (WMO-No. 8, Volume I, Chapter 1).

*Siting classification* (`Annex 1.D, WMO-No. 8, Volume I, Chapter 1 <https://library.wmo.int/idviewer/68695/66>`__)
describes how well the surroundings of the sensor allow a measurement that is
representative of a wide area. It ranges from class 1, a reference site, to
class 5, a site where nearby obstacles make the measurement unrepresentative
of the wider area. A higher class does not mean the data are wrong; the site
may still be valuable for applications that need a measurement at that
location. Each measured variable is classified separately, so the temperature
sensor and the rain gauge at a station can have different classes.

* For **air temperature**, the class depends on the slope and vegetation
  around the screen, the distance to artificial heat sources and reflective
  surfaces (buildings, concrete, car parks) and to expanses of water, and
  shading by nearby obstacles. For example, class 1 requires flat land with
  low natural vegetation, more than 100 m from heat sources and water, and no
  shade when the sun is higher than 5°. Classes 3, 4 and 5 add an estimated
  uncertainty of up to 1 °C, 2 °C and 5 °C respectively.
* For **precipitation**, the class depends mainly on the slope of the land and
  the distance to obstacles relative to their height, since obstacles disturb
  the airflow over the gauge. For example, class 2 requires obstacles to be at
  least twice their height away, and class 5 applies when obstacles are closer
  than half their height. Classes 2 to 5 add an estimated uncertainty of up to
  5 %, 15 %, 25 % and 100 % respectively.

The siting class should be checked visually every year and fully reassessed
at least every five years.

*Measurement quality classification* (`Annex 1.G, WMO-No. 8, Volume I, Chapter 1 <https://library.wmo.int/idviewer/68695/103>`__)
describes the uncertainty achieved by the measurement system itself, independent
of its siting. It takes into account the instrument and its calibration, how it is
coupled to the environment (for example, the type of radiation screen), maintenance and
field verification, and environmental effects on the instrument. The classes
are defined by target uncertainties (95 % confidence) aligned with the WMO
observation requirements:

.. list-table::
   :header-rows: 1
   :widths: 28 18 18 18 18

   * - Measurand
     - Class A
     - Class B
     - Class C
     - Class D
   * - Air temperature
     - 0.2 K
     - 0.6 K
     - 1.0 K
     - Greater than class C, or unknown
   * - Daily accumulated liquid precipitation
     - Greater of 1 mm or 2 %
     - Greater of 3 mm or 5 %
     - Greater of 5 mm or 10 %
     - Greater than class C, or unknown

To keep a class over time, instruments need traceable calibration at suitable
intervals, field verification between calibrations and regular maintenance.

The two classes are combined into a single code, given in the
``temperature_siting_classification`` (BUFR code table 0 08 095) and
``precipitation_siting_classification`` (BUFR code table 0 08 096) columns.
Both code tables use the same codes. Codes 26 - 30 give the siting class only,
and codes 31 - 34 the measurement quality class only.

.. list-table::
   :header-rows: 1
   :stub-columns: 1
   :widths: 30 14 14 14 14 14

   * - Siting class
     - A
     - B
     - C
     - D
     - Quality class not known
   * - 1
     - 1
     - 2
     - 3
     - 4
     - 26
   * - 2
     - 6
     - 7
     - 8
     - 9
     - 27
   * - 3
     - 11
     - 12
     - 13
     - 14
     - 28
   * - 4
     - 16
     - 17
     - 18
     - 19
     - 29
   * - 5
     - 21
     - 22
     - 23
     - 24
     - 30
   * - Siting class not known
     - 31
     - 32
     - 33
     - 34
     - 255 (missing)

Codes 0, 5, 10, 15, 20, 25 and 35 - 254 are reserved.

.. _method-codes:

**Method used to calculate the average daily temperature**

``averaging_method`` uses BUFR code table
0 08 094.

.. list-table::
   :header-rows: 1
   :widths: 10 90

   * - Code
     - Meaning
   * - 0
     - Average of maximum and minimum values: Tm = (Tx + Tn)/2
   * - 1
     - Average of the 8 observations taken every three hours
   * - 2
     - Average of the 24 hourly observations
   * - 3
     - Weighted average of 3 observations: Tm = (aT1 + bT2 + cT3)
   * - 4
     - Weighted average of 3 observations and also maximum and minimum values:
       Tm = (aT1 + bT2 + cT3 + dTx + eTn)
   * - 5
     - Automatic weather station complete integration from minute data
   * - 6
     - Average of the 4 observations taken every six hours
   * - 7
     - Average of the 144 observations taken every 10 minutes
   * - 8 - 254
     - Reserved
   * - 255
     - Missing value

In codes 3 and 4, a - e are the weights given to each temperature, T1 - T3 are
observations at three different times, and Tx and Tn are the daily maximum and
minimum temperatures.

Input CSV
---------

.. note::

   The CSV format described here is defined for this csv2bufr template only.
   It is not a WMO standard. The column names and layout are a convenience
   for preparing data for conversion; the standard is the BUFR sequence
   307095 defined in the *Manual on Codes* (WMO-No. 306), Volume I.2.

File format
^^^^^^^^^^^

* Comma separated (``,``), with no quoting of values.
* One header row containing the column names. Columns are matched by name,
  so their order does not matter, but every column listed below must be
  present.
* One row per station per Attribution day. Each row becomes one subset, and
  all rows in the file are packed into a single BUFR message.
* An empty cell is encoded as missing. Values that are not measured, not
  available or not known should be left empty rather than filled with a
  placeholder such as ``-999``.
* All dates and times are in the station's LMTZ, not UTC.
* Values must be in the units shown. In particular, temperatures are in
  kelvin (K = °C + 273.15), snow depths are in metres and the UTC offset is
  in minutes.
* Temperatures must be given in kelvin to 2 decimal places. A value in °C to
  1 decimal place has 2 decimal places once converted (23.4 °C = 296.55 K).
  Rounding it to 1 decimal place in kelvin (296.6 K) changes the value,
  which then decodes as 23.5 °C.

Station identification and metadata
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

These columns normally repeat on every row for a station. The WIGOS
identifier, ``0-20000-0-71805`` for example, is split across the four ``wsi_*``
columns.

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
     - 0 - 65535
   * - ``wsi_issue_number``
     - WIGOS issue number (third block)
     - 0 - 65535
   * - ``wsi_local``
     - WIGOS local identifier (fourth block), e.g. 71805
     - text, up to 16 characters
   * - ``wmo_block_number``
     - Traditional WMO block number (first two digits of the five-digit station index). Leave empty if the station has none.
     - 0 - 99
   * - ``wmo_station_number``
     - Traditional WMO station number (last three digits of the station index). Leave empty if the station has none.
     - 0 - 999
   * - ``latitude``
     - Station latitude (WGS-84), north positive
     - degrees, 5 decimal places
   * - ``longitude``
     - Station longitude (WGS-84), east positive
     - degrees, 5 decimal places
   * - ``station_height_above_msl``
     - Height of the station ground above mean sea level
     - m, 1 decimal place
   * - ``thermometer_height``
     - Height of the temperature sensor above local ground
     - m, 2 decimal places
   * - ``temperature_siting_classification``
     - Combined siting and measurement quality classification of the temperature sensor
     - BUFR code table 0 08 095 (see `Siting and measurement quality classification <siting-codes_>`__)
   * - ``precipitation_siting_classification``
     - Combined siting and measurement quality classification of the precipitation gauge
     - BUFR code table 0 08 096 (see `Siting and measurement quality classification <siting-codes_>`__)
   * - ``averaging_method``
     - Method used to calculate the daily mean temperature
     - BUFR code table 0 08 094 (see `Method used to calculate the average daily temperature <method-codes_>`__)

Attribution day
^^^^^^^^^^^^^^^

The date that the row's values are attributed to, and the station's offset
from UTC.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``attribution_year``
     - Year of the Attribution day (LMTZ)
     - e.g. 2026
   * - ``attribution_month``
     - Month of the Attribution day (LMTZ)
     - 1 - 12
   * - ``attribution_day``
     - Day of the Attribution day (LMTZ)
     - 1 - 31
   * - ``utc_offset``
     - Time difference LMTZ - UTC, positive east of Greenwich
     - minutes, e.g. 660, 0, -240

Total snow depth
^^^^^^^^^^^^^^^^

Total snow depth is a spot measurement, so only the date and time of the
measurement are given.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year_total_snow_depth``
     - Measurement year (LMTZ)
     - e.g. 2026
   * - ``month_total_snow_depth``
     - Measurement month (LMTZ)
     - 1 - 12
   * - ``day_total_snow_depth``
     - Measurement day (LMTZ)
     - 1 - 31
   * - ``hour_total_snow_depth``
     - Measurement hour (LMTZ)
     - 0 - 23
   * - ``minute_total_snow_depth``
     - Measurement minute (LMTZ)
     - 0 - 59
   * - ``total_snow_depth``
     - Total depth of snow on the ground at the measurement time
     - m
   * - ``total_snow_depth_quality``
     - Quality flag for ``total_snow_depth``
     - BUFR code table 0 31 021 (see `Quality flags`_)

Total accumulated precipitation
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The start and end of the precipitation period, and the total over that
period.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year_precip_accumulation_start``
     - Start of period: year (LMTZ)
     - e.g. 2026
   * - ``month_precip_accumulation_start``
     - Start of period: month (LMTZ)
     - 1 - 12
   * - ``day_precip_accumulation_start``
     - Start of period: day (LMTZ)
     - 1 - 31
   * - ``hour_precip_accumulation_start``
     - Start of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_precip_accumulation_start``
     - Start of period: minute (LMTZ)
     - 0 - 59
   * - ``year_precip_accumulation_end``
     - End of period: year (LMTZ)
     - e.g. 2026
   * - ``month_precip_accumulation_end``
     - End of period: month (LMTZ)
     - 1 - 12
   * - ``day_precip_accumulation_end``
     - End of period: day (LMTZ)
     - 1 - 31
   * - ``hour_precip_accumulation_end``
     - End of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_precip_accumulation_end``
     - End of period: minute (LMTZ)
     - 0 - 59
   * - ``total_acc_precip``
     - Total precipitation accumulated over the period
     - kg m-2 (1 kg m-2 = 1 mm)
   * - ``total_acc_precip_quality``
     - Quality flag for ``total_acc_precip``
     - BUFR code table 0 31 021 (see `Quality flags`_)

Depth of fresh snow
^^^^^^^^^^^^^^^^^^^

The start and end of the fresh snow period, and the depth of fresh snow
accumulated over that period.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year_depth_of_fresh_snow_start``
     - Start of period: year (LMTZ)
     - e.g. 2026
   * - ``month_depth_of_fresh_snow_start``
     - Start of period: month (LMTZ)
     - 1 - 12
   * - ``day_depth_of_fresh_snow_start``
     - Start of period: day (LMTZ)
     - 1 - 31
   * - ``hour_depth_of_fresh_snow_start``
     - Start of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_depth_of_fresh_snow_start``
     - Start of period: minute (LMTZ)
     - 0 - 59
   * - ``year_depth_of_fresh_snow_end``
     - End of period: year (LMTZ)
     - e.g. 2026
   * - ``month_depth_of_fresh_snow_end``
     - End of period: month (LMTZ)
     - 1 - 12
   * - ``day_depth_of_fresh_snow_end``
     - End of period: day (LMTZ)
     - 1 - 31
   * - ``hour_depth_of_fresh_snow_end``
     - End of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_depth_of_fresh_snow_end``
     - End of period: minute (LMTZ)
     - 0 - 59
   * - ``depth_of_fresh_snow``
     - Depth of fresh snow accumulated over the period
     - m
   * - ``depth_of_fresh_snow_quality``
     - Quality flag for ``depth_of_fresh_snow``
     - BUFR code table 0 31 021 (see `Quality flags`_)

Maximum air temperature
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year_tmax_start``
     - Start of period: year (LMTZ)
     - e.g. 2026
   * - ``month_tmax_start``
     - Start of period: month (LMTZ)
     - 1 - 12
   * - ``day_tmax_start``
     - Start of period: day (LMTZ)
     - 1 - 31
   * - ``hour_tmax_start``
     - Start of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_tmax_start``
     - Start of period: minute (LMTZ)
     - 0 - 59
   * - ``year_tmax_end``
     - End of period: year (LMTZ)
     - e.g. 2026
   * - ``month_tmax_end``
     - End of period: month (LMTZ)
     - 1 - 12
   * - ``day_tmax_end``
     - End of period: day (LMTZ)
     - 1 - 31
   * - ``hour_tmax_end``
     - End of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_tmax_end``
     - End of period: minute (LMTZ)
     - 0 - 59
   * - ``air_temperature_maximum``
     - Highest air temperature in the period
     - K, 2 decimal places
   * - ``air_temperature_maximum_quality``
     - Quality flag for ``air_temperature_maximum``
     - BUFR code table 0 31 021 (see `Quality flags`_)

Minimum air temperature
^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year_tmin_start``
     - Start of period: year (LMTZ)
     - e.g. 2026
   * - ``month_tmin_start``
     - Start of period: month (LMTZ)
     - 1 - 12
   * - ``day_tmin_start``
     - Start of period: day (LMTZ)
     - 1 - 31
   * - ``hour_tmin_start``
     - Start of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_tmin_start``
     - Start of period: minute (LMTZ)
     - 0 - 59
   * - ``year_tmin_end``
     - End of period: year (LMTZ)
     - e.g. 2026
   * - ``month_tmin_end``
     - End of period: month (LMTZ)
     - 1 - 12
   * - ``day_tmin_end``
     - End of period: day (LMTZ)
     - 1 - 31
   * - ``hour_tmin_end``
     - End of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_tmin_end``
     - End of period: minute (LMTZ)
     - 0 - 59
   * - ``air_temperature_minimum``
     - Lowest air temperature in the period
     - K, 2 decimal places
   * - ``air_temperature_minimum_quality``
     - Quality flag for ``air_temperature_minimum``
     - BUFR code table 0 31 021 (see `Quality flags`_)

Mean air temperature
^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year_tave_start``
     - Start of period: year (LMTZ)
     - e.g. 2026
   * - ``month_tave_start``
     - Start of period: month (LMTZ)
     - 1 - 12
   * - ``day_tave_start``
     - Start of period: day (LMTZ)
     - 1 - 31
   * - ``hour_tave_start``
     - Start of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_tave_start``
     - Start of period: minute (LMTZ)
     - 0 - 59
   * - ``year_tave_end``
     - End of period: year (LMTZ)
     - e.g. 2026
   * - ``month_tave_end``
     - End of period: month (LMTZ)
     - 1 - 12
   * - ``day_tave_end``
     - End of period: day (LMTZ)
     - 1 - 31
   * - ``hour_tave_end``
     - End of period: hour (LMTZ)
     - 0 - 23
   * - ``minute_tave_end``
     - End of period: minute (LMTZ)
     - 0 - 59
   * - ``air_temperature_average``
     - Mean air temperature over the period, calculated by the method in ``averaging_method``
     - K, 2 decimal places
   * - ``air_temperature_average_quality``
     - Quality flag for ``air_temperature_average``
     - BUFR code table 0 31 021 (see `Quality flags`_)

Notes
-----

.. TODO: add usage notes, known limitations and change history.
