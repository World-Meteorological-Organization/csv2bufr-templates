Surface-RA-IV-100
=================

:Template: :template:`Surface-RA-IV-100.json`
:Version: 1
:BUFR sequence: ``301150, 307084, 014018, 007032, 013155, 007032, 103000, 031001, 007061, 012030, 013111, 007032, 012102, 007032, 004024, 013011``
:Data category / sub-category: 0 / 2
:Header rows: 1 (column names in row 1)
:Sample data: *To be added.*

Mapping template for converting CSV data extracted from SURFACE to sequence 301150, 307084. Additional BUFR descriptors added for WBT, soil moisture, soil temp. and manual precipitation.

Input CSV
---------

.. note::

   The CSV format described here is defined for this csv2bufr template only.
   It is not a WMO standard. The column names and layout are a convenience
   for preparing data for conversion; the standard is the BUFR sequence
   defined in the *Manual on Codes* (WMO-No. 306), Volume I.2.

The CSV is designed for data exported from SURFACE. It covers the synoptic
observation (sequence 307084) together with radiation, precipitation
intensity, soil temperature and moisture, wet-bulb temperature and manual
precipitation. The **FM 12** column gives the corresponding group in the
traditional alphanumeric SYNOP code, to help users converting from TAC.

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
* Values must be in the units shown. Most are SI units, but a few columns
  use the units or codes from FM 12, which the template converts: visibility
  in kilometres, cloud cover in oktas, and cloud type and direction of
  cloud movement as FM 12 code figures.
* Temperatures must be given in kelvin to 2 decimal places. A value in °C to
  1 decimal place has 2 decimal places once converted (23.4 °C = 296.55 K).
  Rounding it to 1 decimal place in kelvin (296.6 K) changes the value,
  which then decodes as 23.5 °C.
* The template encodes exactly four individual cloud layers and two soil
  depths. Leave the columns for unused layers or depths empty.

Station identification and location
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``wsi_series``
     - 
     - WIGOS identifier series (first block of the WSI)
     - 0
   * - ``wsi_issuer``
     - 
     - WIGOS issuer of identifier (second block)
     - 0 - 65534
   * - ``wsi_issue_number``
     - 
     - WIGOS issue number (third block)
     - 0 - 65534
   * - ``wsi_local``
     - 
     - WIGOS local identifier (fourth block)
     - text, up to 16 characters
   * - ``wmo_block_number``
     - II
     - Traditional WMO block number. Leave empty if the station has none.
     - 0 - 99
   * - ``wmo_station_number``
     - iii
     - Traditional WMO station number. Leave empty if the station has none.
     - 0 - 999
   * - ``station_type``
     - 
     - Type of observing station (BUFR code table 0 02 001)
     - 0 = automatic, 1 = manned, 2 = hybrid (both manned and automatic)
   * - ``latitude``
     - 
     - Latitude of the station
     - degrees north, 5 decimal places
   * - ``longitude``
     - 
     - Longitude of the station
     - degrees east, 5 decimal places
   * - ``station_height_above_msl``
     - 
     - Height of the station ground above mean sea level
     - m, 1 decimal place
   * - ``barometer_height_above_msl``
     - 
     - Height of the barometer above mean sea level, typically the height of the station ground plus the height of the sensor above local ground
     - m, 1 decimal place

Time of observation
^^^^^^^^^^^^^^^^^^^

The time of observation is based on the actual time the barometer is read.

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``year``
     - 
     - Year of observation (UTC)
     - e.g. 2026
   * - ``month``
     - 
     - Month of observation (UTC)
     - 1 - 12
   * - ``day``
     - YY
     - Day of observation (UTC)
     - 1 - 31
   * - ``hour``
     - GG
     - Hour of observation (UTC)
     - 0 - 23
   * - ``minute``
     - gg
     - Minute of observation (UTC)
     - 0 - 59

Pressure
^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``station_pressure``
     - P0P0P0P0
     - Pressure observed at station level
     - Pa, to the nearest 10 Pa
   * - ``msl_pressure``
     - PPPP
     - Pressure reduced to mean sea level
     - Pa, to the nearest 10 Pa
   * - ``24_hour_barometric_change``
     - p24p24p24
     - Pressure change over the preceding 24 hours
     - Pa, to the nearest 10 Pa
   * - ``geopotential_height``
     - hhh
     - Geopotential height of a standard pressure level, for stations that report this instead of mean sea level pressure
     - gpm, 0 decimal places

Temperature and humidity
^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``thermometer_height``
     - 
     - Height of the thermometer / temperature sensor above local ground. Also used for the extreme and wet-bulb temperatures.
     - m, 2 decimal places
   * - ``air_temperature``
     - TTT
     - Instantaneous air temperature
     - K, 2 decimal places
   * - ``dewpoint_temperature``
     - TdTdTd
     - Instantaneous dewpoint temperature
     - K, 2 decimal places
   * - ``relative_humidity``
     - UUU
     - Instantaneous relative humidity
     - %, 0 decimal places
   * - ``wetbulb_temperature``
     - 
     - Wet-bulb temperature
     - K, 2 decimal places
   * - ``maximum_air_temperature``
     - TxTxTx
     - Maximum air temperature over the preceding 12 hours
     - K, 2 decimal places
   * - ``minimum_air_temperature``
     - TnTnTn
     - Minimum air temperature over the preceding 12 hours
     - K, 2 decimal places

Visibility
^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``visibility``
     - VV
     - Horizontal visibility. Given in kilometres; the template converts to metres. The height of the visibility sensor is set to 1.7 m by the template.
     - km

Clouds
^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``cloud_cover_tot``
     - N
     - Total cloud cover. Given in oktas; the template converts to per cent.
     - oktas, 0 - 8
   * - ``observed_cloud_coverage``
     - Nh
     - Amount of all the CL clouds present or, if there are none, all the CM clouds present (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``lowest_cloud_height``
     - h
     - Height of the base of the lowest cloud
     - m
   * - ``low_cloud_type``
     - CL
     - Type of low cloud, using the FM 12 CL code. The template converts it to BUFR code table 0 20 012.
     - 0 - 9
   * - ``middle_cloud_type``
     - CM
     - Type of middle cloud, using the FM 12 CM code. The template converts it to BUFR code table 0 20 012.
     - 0 - 9
   * - ``high_cloud_type``
     - CH
     - Type of high cloud, using the FM 12 CH code. The template converts it to BUFR code table 0 20 012.
     - 0 - 9
   * - ``cloud_coverage_l1``
     - Ns
     - Amount of cloud in layer 1 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``genus_of_cloud_l1``
     - C
     - Genus of the cloud in layer 1 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``height_of_cloud_base_l1``
     - hshs
     - Height of the base of the cloud in layer 1
     - m
   * - ``cloud_coverage_l2``
     - Ns
     - Amount of cloud in layer 2 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``genus_of_cloud_l2``
     - C
     - Genus of the cloud in layer 2 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``height_of_cloud_base_l2``
     - hshs
     - Height of the base of the cloud in layer 2
     - m
   * - ``cloud_coverage_l3``
     - Ns
     - Amount of cloud in layer 3 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``genus_of_cloud_l3``
     - C
     - Genus of the cloud in layer 3 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``height_of_cloud_base_l3``
     - hshs
     - Height of the base of the cloud in layer 3
     - m
   * - ``cloud_coverage_l4``
     - Ns
     - Amount of cloud in layer 4 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``genus_of_cloud_l4``
     - C
     - Genus of the cloud in layer 4 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``height_of_cloud_base_l4``
     - hshs
     - Height of the base of the cloud in layer 4
     - m
   * - ``direction_of_cl_clouds``
     - DL
     - Direction from which the low clouds are moving, using the FM 12 direction code. The template converts it to degrees.
     - 1 = NE, 2 = E, 3 = SE, 4 = S, 5 = SW, 6 = W, 7 = NW, 8 = N
   * - ``direction_of_cm_clouds``
     - DM
     - Direction from which the middle clouds are moving, using the FM 12 direction code. The template converts it to degrees.
     - as for ``direction_of_cl_clouds``
   * - ``direction_of_ch_clouds``
     - DH
     - Direction from which the high clouds are moving, using the FM 12 direction code. The template converts it to degrees.
     - as for ``direction_of_cl_clouds``

Weather, state of ground and snow
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``present_weather``
     - ww
     - Present weather (BUFR code table 0 20 003). Codes 0 - 99 are for manned stations and 100 - 199 for automatic stations.
     - code
   * - ``past_weather_w_1``
     - W1
     - Past weather, first type (BUFR code table 0 20 004). Codes 0 - 9 are for manned stations and 10 - 19 for automatic stations.
     - code
   * - ``past_weather_w_2``
     - W2
     - Past weather, second type (BUFR code table 0 20 005)
     - code
   * - ``state_of_sky``
     - 
     - State of sky in the tropics (BUFR code table 0 20 055)
     - 0 - 10
   * - ``ground_state``
     - E or E'
     - State of the ground, with or without snow (BUFR code table 0 20 062)
     - code
   * - ``snow_depth``
     - sss
     - Total snow depth at the time of observation
     - m, 2 decimal places

Precipitation
^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``rain_sensor_height``
     - 
     - Height of the precipitation gauge rim above local ground. Used for all the precipitation values.
     - m, 2 decimal places
   * - ``total_precipitation_1_hour``
     - RRR
     - Total precipitation over the preceding hour
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_6_hours``
     - RRR
     - Total precipitation over the preceding 6 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_24_hours``
     - R24R24R24R24
     - Total precipitation over the preceding 24 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``precipitation_intensity``
     - 
     - Intensity of precipitation at the time of observation
     - kg m-2 s-1, 5 decimal places
   * - ``precipitation_period_duration``
     - tR
     - Length of the period covered by ``precipitation``, as a negative number of hours before the observation time (e.g. -3)
     - hours, -24 to -1
   * - ``precipitation``
     - RRR
     - Total precipitation over the period given in ``precipitation_period_duration``, for example from a manual gauge
     - kg m-2 (= mm), 1 decimal place

Wind
^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``anemometer_height``
     - 
     - Height of the anemometer above local ground
     - m, 2 decimal places
   * - ``time_period_of_wind``
     - 
     - Period over which the wind speed and direction have been averaged, given as a negative number of minutes before the observation time. Normally -10, or the number of minutes since a significant change in the preceding 10 minutes.
     - min, -10 to 0
   * - ``wind_direction``
     - dd
     - Wind direction at anemometer height, averaged over the averaging period
     - degrees, 0 decimal places
   * - ``wind_speed``
     - ff
     - Wind speed at anemometer height, averaged over the averaging period
     - m s-1, 1 decimal place
   * - ``maximum_wind_gust_direction_10_minutes``
     - 
     - Direction of the maximum wind gust over the preceding 10 minutes
     - degrees, 0 decimal places
   * - ``maximum_wind_gust_speed_10_minutes``
     - fmfm
     - Maximum wind gust speed (highest 3-second average) over the preceding 10 minutes
     - m s-1, 1 decimal place
   * - ``maximum_wind_gust_direction_1_hour``
     - 
     - Direction of the maximum wind gust over the preceding hour
     - degrees, 0 decimal places
   * - ``maximum_wind_gust_speed_1_hour``
     - fxfx
     - Maximum wind gust speed (highest 3-second average) over the preceding hour
     - m s-1, 1 decimal place

Radiation and soil
^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``solar_radiation``
     - 
     - Instantaneous short-wave radiation
     - W m-2
   * - ``soil_temperature_depth_1``
     - 
     - Depth below the land surface of the first soil measurement
     - m, 2 decimal places
   * - ``soil_temperature_1``
     - 
     - Soil temperature at the first depth
     - K, 1 decimal place
   * - ``soil_moisture_1``
     - 
     - Soil moisture at the first depth
     - g kg-1
   * - ``soil_temperature_depth_2``
     - 
     - Depth below the land surface of the second soil measurement
     - m, 2 decimal places
   * - ``soil_temperature_2``
     - 
     - Soil temperature at the second depth
     - K, 1 decimal place
   * - ``soil_moisture_2``
     - 
     - Soil moisture at the second depth
     - g kg-1


Notes
-----

.. TODO: add usage notes, known limitations and change history.
