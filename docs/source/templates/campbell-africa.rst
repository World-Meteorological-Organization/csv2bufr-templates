Surface land stations (Campbell - Africa)
=========================================

:Template: :template:`CampbellAfrica-v1-template.json`
:Version: 1
:BUFR sequence: ``301150, 307080``
:Data category / sub-category: 0 / 6
:Header rows: 4 (column names in row 2)
:Sample data: *To be added.*

Mapping template for converting CSV data from Campbell data loggers configured and deployed in Africa to BUFR seqeunce 301150, 307080.

Input CSV
---------

.. note::

   The CSV format described here is defined for this csv2bufr template only.
   It is not a WMO standard. The column names and layout are a convenience
   for preparing data for conversion; the standard is the BUFR sequence
   defined in the *Manual on Codes* (WMO-No. 306), Volume I.2.

The CSV is the data table written by Campbell Scientific data loggers
configured for deployment in Africa (TOA5 format). Values are given in the
units used by BUFR, so no conversion is applied by the template.

File format
^^^^^^^^^^^

* Comma separated (``,``).
* Four header rows, as written by the logger. The column names are in the
  second row; the other header rows are skipped.
* Columns are matched by name, so their order does not matter, but every
  column listed below must be present. Other columns written by the logger
  are ignored.
* One row per station per observation time. Each row is encoded as a
  separate BUFR message.
* An empty cell is encoded as missing.
* All dates and times are in UTC.
* Values must be in the units shown. In particular, pressures are in pascals
  and temperatures are in kelvin (K = °C + 273.15).
* Temperatures must be given in kelvin to 2 decimal places. A value in °C to
  1 decimal place has 2 decimal places once converted (23.4 °C = 296.55 K).
  Rounding it to 1 decimal place in kelvin (296.6 K) changes the value,
  which then decodes as 23.5 °C.

Station identification and location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``Station_ID``
     - WIGOS station identifier, written in full (e.g. ``0-20000-0-63742``). csv2bufr splits it into its four blocks.
     - text
   * - ``Station_Name``
     - Name of the station
     - text
   * - ``WMO_Station_Type``
     - Type of observing station (BUFR code table 0 02 001)
     - 0 = automatic, 1 = manned, 2 = hybrid (both manned and automatic)
   * - ``Latitude``
     - Latitude of the station
     - degrees north, 5 decimal places
   * - ``Longitude``
     - Longitude of the station
     - degrees east, 5 decimal places
   * - ``Elevation``
     - Height of the station ground above mean sea level
     - m, 1 decimal place
   * - ``BP_Elevation``
     - Height of the barometer above mean sea level
     - m, 1 decimal place

Time of observation
^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``M_Year``
     - Year of observation (UTC)
     - e.g. 2024
   * - ``M_Month``
     - Month of observation (UTC)
     - 1 - 12
   * - ``M_DayOfMonth``
     - Day of observation (UTC)
     - 1 - 31
   * - ``M_HourOfDay``
     - Hour of observation (UTC)
     - 0 - 23
   * - ``M_Minutes``
     - Minute of observation (UTC)
     - 0 - 59

Pressure
^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``BP``
     - Pressure observed at station level
     - Pa, to the nearest 10 Pa
   * - ``QNH``
     - Pressure reduced to mean sea level
     - Pa, to the nearest 10 Pa
   * - ``BP_Change``
     - Pressure change over the preceding 3 hours
     - Pa, to the nearest 10 Pa
   * - ``BP_Tendency``
     - Characteristic of pressure tendency (BUFR code table 0 10 063)
     - code, 0 - 8

Temperature and humidity
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``Temp_H``
     - Height of the temperature sensor above local ground. Also used for the maximum and minimum temperatures.
     - m, 2 decimal places
   * - ``AirTempK``
     - Air temperature
     - K, 2 decimal places
   * - ``DewPointTempK``
     - Dewpoint temperature
     - K, 2 decimal places
   * - ``RH``
     - Relative humidity
     - %, 0 decimal places
   * - ``Temp_hr24``
     - Start of the period for the maximum and minimum temperatures, in hours relative to the observation time (e.g. -24)
     - hours
   * - ``Temp24T``
     - End of the period for the maximum and minimum temperatures, in hours relative to the observation time (e.g. 0)
     - hours
   * - ``AirTempMaxK``
     - Maximum air temperature over the period
     - K, 2 decimal places
   * - ``AirTempMinK``
     - Minimum air temperature over the period
     - K, 2 decimal places

Sunshine
^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``Sun_hr``
     - Period covered by ``SunHrs``, as a negative number of hours before the observation time (e.g. -1)
     - hours
   * - ``SunHrs``
     - Total sunshine over the period. Note that, despite the column name, the value is in minutes.
     - minutes
   * - ``Sun_hr24``
     - Period covered by ``SunHrs24``, as a negative number of hours before the observation time (e.g. -24)
     - hours
   * - ``SunHrs24``
     - Total sunshine over the period. Note that, despite the column name, the value is in minutes.
     - minutes

Precipitation
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``Rain_H``
     - Height of the precipitation gauge rim above local ground
     - m, 2 decimal places
   * - ``Rain_hr``
     - Period covered by ``Rain_mm_Tot``, as a negative number of hours before the observation time (e.g. -1)
     - hours
   * - ``Rain_mm_Tot``
     - Total precipitation over the period
     - kg m-2 (= mm), 1 decimal place

Wind
^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``WSpeed_height``
     - Height of the anemometer above local ground
     - m, 2 decimal places
   * - ``Wind_Type``
     - Type of instrumentation for wind measurement (BUFR flag table 0 02 002). Add the values of the flags that apply: 8 = certified instruments, 4 = originally measured in knots, 2 = originally measured in km h-1.
     - 0 - 15
   * - ``Wind_Sig``
     - Time significance of the wind averaging period (BUFR code table 0 08 021), normally 2 = time averaged
     - code
   * - ``Wind_T``
     - Period over which the wind speed and direction have been averaged, as a negative number of minutes before the observation time (normally -10)
     - minutes
   * - ``WindDir``
     - Wind direction, averaged over the period
     - degrees, 0 decimal places
   * - ``WSpeed10M_Avg``
     - Wind speed, averaged over the period
     - m s-1, 1 decimal place
   * - ``WindG_Sig``
     - Time significance for the wind gust (BUFR code table 0 08 021)
     - code
   * - ``WindGust``
     - Maximum wind gust speed
     - m s-1, 1 decimal place

Radiation
^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``Solar_hr``
     - Period covered by ``SlrJ``, as a negative number of hours before the observation time (e.g. -1)
     - hours
   * - ``SlrJ``
     - Global solar radiation, integrated over the period
     - J m-2
   * - ``Solar_hr24``
     - Period covered by ``SlrJ24``, as a negative number of hours before the observation time (e.g. -24)
     - hours
   * - ``SlrJ24``
     - Global solar radiation, integrated over the period
     - J m-2


Notes
-----

.. TODO: add usage notes, known limitations and change history.
