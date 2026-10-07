Surface land stations (AWS)
===========================

:Template: :template:`aws-template.json`
:Version: 6
:BUFR sequence: ``301150, 307096``
:Data category / sub-category: 0 / 2
:Header rows: 1 (column names in row 1)
:Sample data: :sample:`aws_sample.csv`

Mapping template for converting CSV data from simplified automatic weather station file to BUFR sequence 301150, 307096

Input CSV
---------

.. note::

   The CSV format described here is defined for this csv2bufr template only.
   It is not a WMO standard. The column names and layout are a convenience
   for preparing data for conversion; the standard is the BUFR sequence
   defined in the *Manual on Codes* (WMO-No. 306), Volume I.2.

File format
^^^^^^^^^^^

* Comma separated (``,``), with no quoting of values.
* One header row containing the column names. Columns are matched by name,
  so their order does not matter, but every column listed below must be
  present.
* One row per station per observation time. Each row is encoded as a
  separate BUFR message.
* An empty cell is encoded as missing. Values that are not measured, not
  available or not known should be left empty.
* All dates and times are in UTC.
* Values must be in the units shown. In particular, pressures are in pascals,
  temperatures are in kelvin (K = °C + 273.15) and snow depth is in metres.
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
   * - ``wsi_series``
     - WIGOS identifier series (first block of the WSI)
     - 0
   * - ``wsi_issuer``
     - WIGOS issuer of identifier (second block)
     - 0 - 65534
   * - ``wsi_issue_number``
     - WIGOS issue number (third block)
     - 0 - 65534
   * - ``wsi_local``
     - WIGOS local identifier (fourth block)
     - text, up to 16 characters
   * - ``wmo_block_number``
     - Traditional WMO block number. Leave empty if the station has none.
     - 0 - 99
   * - ``wmo_station_number``
     - Traditional WMO station number. Leave empty if the station has none.
     - 0 - 999
   * - ``station_type``
     - Type of observing station (BUFR code table 0 02 001)
     - 0 = automatic, 1 = manned, 2 = hybrid (both manned and automatic)
   * - ``latitude``
     - Latitude of the station
     - degrees north, 5 decimal places
   * - ``longitude``
     - Longitude of the station
     - degrees east, 5 decimal places
   * - ``station_height_above_msl``
     - Height of the station ground above mean sea level
     - m, 1 decimal place
   * - ``barometer_height_above_msl``
     - Height of the barometer above mean sea level, typically the height of the station ground plus the height of the sensor above local ground
     - m, 1 decimal place

Time of observation
^^^^^^^^^^^^^^^^^^^

The time of observation is based on the actual time the barometer is read.

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``year``
     - Year of observation (UTC)
     - e.g. 2025
   * - ``month``
     - Month of observation (UTC)
     - 1 - 12
   * - ``day``
     - Day of observation (UTC)
     - 1 - 31
   * - ``hour``
     - Hour of observation (UTC)
     - 0 - 23
   * - ``minute``
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
   * - ``station_pressure``
     - Pressure observed at station level
     - Pa, to the nearest 10 Pa
   * - ``msl_pressure``
     - Pressure reduced to mean sea level
     - Pa, to the nearest 10 Pa
   * - ``geopotential_height``
     - Geopotential height of a standard pressure level, for stations that report this instead of mean sea level pressure
     - gpm, 0 decimal places

Temperature and humidity
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``thermometer_height``
     - Height of the thermometer / temperature sensor above local ground
     - m, 2 decimal places
   * - ``air_temperature``
     - Instantaneous air temperature
     - K, 2 decimal places
   * - ``dewpoint_temperature``
     - Instantaneous dewpoint temperature
     - K, 2 decimal places
   * - ``relative_humidity``
     - Instantaneous relative humidity
     - %, 0 decimal places

State of ground and snow depth
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``method_of_ground_state_measurement``
     - Method used to observe the state of the ground (BUFR code table 0 02 176)
     - code
   * - ``ground_state``
     - State of the ground (BUFR code table 0 20 062)
     - code
   * - ``method_of_snow_depth_measurement``
     - Method used to measure the snow depth (BUFR code table 0 02 177)
     - code
   * - ``snow_depth``
     - Total snow depth at the time of observation
     - m, 2 decimal places

Wind
^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``anemometer_height``
     - Height of the anemometer above local ground
     - m, 2 decimal places
   * - ``time_period_of_wind``
     - Period over which the wind speed and direction have been averaged, given as a negative number of minutes before the observation time. Normally -10, or the number of minutes since a significant change in the preceding 10 minutes.
     - min, -10 to 0
   * - ``wind_direction``
     - Wind direction at anemometer height, averaged from the Cartesian components over the averaging period
     - degrees, 0 decimal places
   * - ``wind_speed``
     - Wind speed at anemometer height, averaged from the Cartesian components over the averaging period
     - m s-1, 1 decimal place
   * - ``maximum_wind_gust_direction_10_minutes``
     - Direction of the maximum wind gust over the preceding 10 minutes
     - degrees, 0 decimal places
   * - ``maximum_wind_gust_speed_10_minutes``
     - Maximum wind gust speed (highest 3-second average) over the preceding 10 minutes
     - m s-1, 1 decimal place
   * - ``maximum_wind_gust_direction_1_hour``
     - Direction of the maximum wind gust over the preceding hour
     - degrees, 0 decimal places
   * - ``maximum_wind_gust_speed_1_hour``
     - Maximum wind gust speed (highest 3-second average) over the preceding hour
     - m s-1, 1 decimal place
   * - ``maximum_wind_gust_direction_3_hours``
     - Direction of the maximum wind gust over the preceding 3 hours
     - degrees, 0 decimal places
   * - ``maximum_wind_gust_speed_3_hours``
     - Maximum wind gust speed (highest 3-second average) over the preceding 3 hours
     - m s-1, 1 decimal place

Precipitation
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 50 20

   * - Column
     - Description
     - Units / values
   * - ``rain_sensor_height``
     - Height of the precipitation gauge rim above local ground
     - m, 2 decimal places
   * - ``precipitation_intensity``
     - Intensity of precipitation at the time of observation
     - kg m-2 s-1, 5 decimal places
   * - ``total_precipitation_1_hour``
     - Total precipitation over the preceding hour
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_3_hours``
     - Total precipitation over the preceding 3 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_6_hours``
     - Total precipitation over the preceding 6 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_12_hours``
     - Total precipitation over the preceding 12 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_24_hours``
     - Total precipitation over the preceding 24 hours
     - kg m-2 (= mm), 1 decimal place


Notes
-----

.. TODO: add usage notes, known limitations and change history.
