Surface land stations export from Climsoft CDMS
===============================================

:Template: :template:`Climsoft-hourly.json`
:Version: 1
:BUFR sequence: ``301150, 307080, 002176, 002177, 302040, 004024, 101010, 307063``
:Data category / sub-category: 0 / 2
:Header rows: 1 (column names in row 1)
:Sample data: :sample:`climsoft.csv`

Mapping template for converting CSV data from Climsoft to BUFR sequence 301150, 307080, 002176, 002177, 302040, 004024, 101010, 307063

Input CSV
---------

.. note::

   The CSV format described here is defined for this csv2bufr template only.
   It is not a WMO standard. The column names and layout are a convenience
   for preparing data for conversion; the standard is the BUFR sequence
   defined in the *Manual on Codes* (WMO-No. 306), Volume I.2.

The CSV is designed for hourly data exported from the Climsoft climate data
management system. Values are given in the units and code tables used by
BUFR, so no conversion is applied by the template. The **FM 12** column gives
the corresponding group in the traditional alphanumeric SYNOP code, to help
users converting from TAC.

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
* All dates and times are in UTC. Periods are given as a negative number of
  hours before the observation time (e.g. ``-6`` for the preceding 6 hours).
* Values must be in the units shown. In particular, pressures are in pascals,
  temperatures are in kelvin (K = °C + 273.15), cloud cover is in per cent
  and visibility is in metres.
* Temperatures must be given in kelvin to 2 decimal places. A value in °C to
  1 decimal place has 2 decimal places once converted (23.4 °C = 296.55 K).
  Rounding it to 1 decimal place in kelvin (296.6 K) changes the value,
  which then decodes as 23.5 °C.
* The template encodes exactly four individual cloud layers and ten soil
  levels. Leave the columns for unused layers or levels empty.

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
   * - ``station_name``
     - 
     - Name of the station
     - text
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
     - Height of the barometer above mean sea level
     - m, 1 decimal place

Time of observation
^^^^^^^^^^^^^^^^^^^

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
   * - ``pressure_change_3hr``
     - ppp
     - Pressure change over the preceding 3 hours
     - Pa, to the nearest 10 Pa
   * - ``pressure_tendency_characteristic``
     - a
     - Characteristic of pressure tendency (BUFR code table 0 10 063)
     - code, 0 - 8
   * - ``pressure_change_24hr``
     - p24p24p24
     - Pressure change over the preceding 24 hours
     - Pa, to the nearest 10 Pa
   * - ``pressure_standard_level``
     - a3
     - Standard pressure level for which ``geopotential_height`` is reported, for stations that report geopotential instead of mean sea level pressure
     - Pa
   * - ``geopotential_height``
     - hhh
     - Geopotential height of the standard pressure level
     - gpm

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
     - Height of the thermometer / temperature sensor above local ground
     - m, 2 decimal places
   * - ``air_temperature``
     - TTT
     - Air temperature
     - K, 2 decimal places
   * - ``dewpoint_temperature``
     - TdTdTd
     - Dewpoint temperature
     - K, 2 decimal places
   * - ``relative_humidity``
     - UUU
     - Relative humidity
     - %, 0 decimal places
   * - ``extreme_temp_sensor_height``
     - 
     - Height of the sensor used for the maximum and minimum temperatures
     - m, 2 decimal places
   * - ``temp_max_period``
     - 
     - Start of the period for ``temp_maximum``, as a negative number of hours before the observation time (the period ends at the observation time)
     - hours, negative (e.g. -24)
   * - ``temp_maximum``
     - TxTxTx
     - Maximum air temperature over the period
     - K, 2 decimal places
   * - ``temp_min_period``
     - 
     - Start of the period for ``temp_minimum``, as a negative number of hours before the observation time (the period ends at the observation time)
     - hours, negative (e.g. -24)
   * - ``temp_minimum``
     - TnTnTn
     - Minimum air temperature over the period
     - K, 2 decimal places
   * - ``ground_minimum_temperature``
     - TgTg
     - Ground minimum temperature over the preceding 12 hours
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
   * - ``visibility_sensor_height``
     - 
     - Height of the visibility sensor above local ground
     - m, 2 decimal places
   * - ``horizontal_visibility``
     - VV
     - Horizontal visibility
     - m, to the nearest 10 m

Clouds
^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``cloud_total_cover``
     - N
     - Total cloud cover
     - %, 0 - 100
   * - ``cloud_total_vertical_sig``
     - 
     - Vertical significance of the cloud reported in ``cloud_amount_low_level`` (BUFR code table 0 08 002), e.g. 7 = low cloud, 8 = middle cloud
     - code
   * - ``cloud_amount_low_level``
     - Nh
     - Amount of all the CL clouds present or, if there are none, all the CM clouds present (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``cloud_base_height``
     - h
     - Height of the base of the lowest cloud
     - m
   * - ``cloud_type_low_level``
     - CL
     - Type of low cloud (BUFR code table 0 20 012)
     - 30 - 39 (FM 12 CL + 30)
   * - ``cloud_type_mid_level``
     - CM
     - Type of middle cloud (BUFR code table 0 20 012)
     - 20 - 29 (FM 12 CM + 20)
   * - ``cloud_type_high_level``
     - CH
     - Type of high cloud (BUFR code table 0 20 012)
     - 10 - 19 (FM 12 CH + 10)
   * - ``cloud_layer1_vertical_sig``
     - 
     - Vertical significance of cloud layer 1 (BUFR code table 0 08 002), e.g. 1 = first individual layer
     - code
   * - ``cloud_layer1_amount``
     - Ns
     - Amount of cloud in layer 1 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``cloud_layer1_type``
     - C
     - Genus of the cloud in layer 1 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``cloud_layer1_base_height``
     - hshs
     - Height of the base of the cloud in layer 1
     - m
   * - ``cloud_layer2_vertical_sig``
     - 
     - Vertical significance of cloud layer 2 (BUFR code table 0 08 002), e.g. 1 = first individual layer
     - code
   * - ``cloud_layer2_amount``
     - Ns
     - Amount of cloud in layer 2 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``cloud_layer2_type``
     - C
     - Genus of the cloud in layer 2 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``cloud_layer2_base_height``
     - hshs
     - Height of the base of the cloud in layer 2
     - m
   * - ``cloud_layer3_vertical_sig``
     - 
     - Vertical significance of cloud layer 3 (BUFR code table 0 08 002), e.g. 1 = first individual layer
     - code
   * - ``cloud_layer3_amount``
     - Ns
     - Amount of cloud in layer 3 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``cloud_layer3_type``
     - C
     - Genus of the cloud in layer 3 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``cloud_layer3_base_height``
     - hshs
     - Height of the base of the cloud in layer 3
     - m
   * - ``cloud_layer4_vertical_sig``
     - 
     - Vertical significance of cloud layer 4 (BUFR code table 0 08 002), e.g. 1 = first individual layer
     - code
   * - ``cloud_layer4_amount``
     - Ns
     - Amount of cloud in layer 4 (BUFR code table 0 20 011)
     - oktas, 0 - 8; 9 = sky obscured
   * - ``cloud_layer4_type``
     - C
     - Genus of the cloud in layer 4 (BUFR code table 0 20 012)
     - 0 = Ci, 1 = Cc, 2 = Cs, 3 = Ac, 4 = As, 5 = Ns, 6 = Sc, 7 = St, 8 = Cu, 9 = Cb
   * - ``cloud_layer4_base_height``
     - hshs
     - Height of the base of the cloud in layer 4
     - m

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
   * - ``past_weather_period``
     - 
     - Period covered by the past weather, as a negative number of hours before the observation time
     - hours, e.g. -6 or -3
   * - ``past_weather1``
     - W1
     - Past weather, first type (BUFR code table 0 20 004). Codes 0 - 9 are for manned stations and 10 - 19 for automatic stations.
     - code
   * - ``past_weather2``
     - W2
     - Past weather, second type (BUFR code table 0 20 005)
     - code
   * - ``method_of_ground_state_measurement``
     - 
     - Method used to observe the state of the ground (BUFR code table 0 02 176)
     - code
   * - ``ground_state``
     - E or E'
     - State of the ground, with or without snow (BUFR code table 0 20 062)
     - code
   * - ``method_of_snow_depth_measurement``
     - 
     - Method used to measure the snow depth (BUFR code table 0 02 177)
     - code
   * - ``snow_depth``
     - sss
     - Total snow depth
     - m, 2 decimal places

Sunshine
^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``sunshine_total_1hr``
     - SS
     - Total sunshine over the preceding hour
     - minutes
   * - ``sunshine_total_24hr``
     - SSS
     - Total sunshine over the preceding 24 hours
     - minutes

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
   * - ``total_precipitation_3_hour``
     - RRR
     - Total precipitation over the preceding 3 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_6_hour``
     - RRR
     - Total precipitation over the preceding 6 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_12_hour``
     - RRR
     - Total precipitation over the preceding 12 hours
     - kg m-2 (= mm), 1 decimal place
   * - ``total_precipitation_24_hour``
     - R24R24R24R24
     - Total precipitation over the preceding 24 hours
     - kg m-2 (= mm), 1 decimal place

Wind
^^^^

The wind speed and direction are averaged over the preceding 10 minutes;
this is set by the template.

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
   * - ``wind_instrument_type``
     - iw
     - Type of instrumentation for wind measurement (BUFR flag table 0 02 002). Add the values of the flags that apply: 8 = certified instruments, 4 = originally measured in knots, 2 = originally measured in km h-1.
     - 0 - 15
   * - ``wind_direction``
     - dd
     - Wind direction, averaged over the preceding 10 minutes
     - degrees, 0 decimal places
   * - ``wind_speed``
     - ff
     - Wind speed, averaged over the preceding 10 minutes
     - m s-1, 1 decimal place
   * - ``max_wind_gust_direction_10min``
     - 
     - Direction of the maximum wind gust over the preceding 10 minutes
     - degrees, 0 decimal places
   * - ``maximum_wind_gust_speed_10min``
     - fmfm
     - Maximum wind gust speed over the preceding 10 minutes
     - m s-1, 1 decimal place
   * - ``max_wind_gust_direction_60min``
     - 
     - Direction of the maximum wind gust over the preceding hour
     - degrees, 0 decimal places
   * - ``maximum_wind_gust_speed_60min``
     - fxfx
     - Maximum wind gust speed over the preceding hour
     - m s-1, 1 decimal place

Evaporation
^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``evaporation_sensor_height``
     - 
     - Height of the evaporation instrument above local ground
     - m, 2 decimal places
   * - ``evaporation_time_period``
     - 
     - Period covered by ``evaporation_total``, as a negative number of hours before the observation time
     - hours, negative (e.g. -24)
   * - ``evaporation_sensor_type``
     - iE
     - Type of instrumentation for evaporation measurement (BUFR code table 0 02 004)
     - code
   * - ``evaporation_total``
     - EEE
     - Evaporation or evapotranspiration over the period
     - kg m-2 (= mm), 1 decimal place

Radiation
^^^^^^^^^

Two sets of radiation values can be given, each with its own period. Leave
any components that are not measured empty.

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``solar_radiation1_time_period``
     - 
     - Period covered by the first set of radiation values, as a negative number of hours before the observation time (normally -1)
     - hours, negative (e.g. -24)
   * - ``solar_radiation1_long_wave``
     - 
     - Long-wave radiation, integrated over the period
     - J m-2
   * - ``solar_radiation1_short_wave``
     - 
     - Short-wave radiation, integrated over the period
     - J m-2
   * - ``solar_radiation1_net``
     - 
     - Net radiation, integrated over the period
     - J m-2
   * - ``solar_radiation1_global``
     - 
     - Global solar radiation, integrated over the period
     - J m-2
   * - ``solar_radiation1_diffuse``
     - 
     - Diffuse solar radiation, integrated over the period
     - J m-2
   * - ``solar_radiation1_direct``
     - 
     - Direct solar radiation, integrated over the period
     - J m-2
   * - ``solar_radiation24_time_period``
     - 
     - Period covered by the second set of radiation values, as a negative number of hours before the observation time (normally -24)
     - hours, negative (e.g. -24)
   * - ``solar_radiation24_long_wave``
     - 
     - Long-wave radiation, integrated over the period
     - J m-2
   * - ``solar_radiation24_short_wave``
     - 
     - Short-wave radiation, integrated over the period
     - J m-2
   * - ``solar_radiation24_net``
     - 
     - Net radiation, integrated over the period
     - J m-2
   * - ``solar_radiation24_global``
     - 
     - Global solar radiation, integrated over the period
     - J m-2
   * - ``solar_radiation24_diffuse``
     - 
     - Diffuse solar radiation, integrated over the period
     - J m-2
   * - ``solar_radiation24_direct``
     - 
     - Direct solar radiation, integrated over the period
     - J m-2

Soil temperature
^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - FM 12
     - Description
     - Units / values
   * - ``soil_level1_depth``
     - 
     - Depth below the land surface of soil level 1
     - m, 2 decimal places
   * - ``soil_level1_temperature``
     - 
     - Soil temperature at level 1
     - K, 2 decimal places
   * - ``soil_level2_depth``
     - 
     - Depth below the land surface of soil level 2
     - m, 2 decimal places
   * - ``soil_level2_temperature``
     - 
     - Soil temperature at level 2
     - K, 2 decimal places
   * - ``soil_level3_depth``
     - 
     - Depth below the land surface of soil level 3
     - m, 2 decimal places
   * - ``soil_level3_temperature``
     - 
     - Soil temperature at level 3
     - K, 2 decimal places
   * - ``soil_level4_depth``
     - 
     - Depth below the land surface of soil level 4
     - m, 2 decimal places
   * - ``soil_level4_temperature``
     - 
     - Soil temperature at level 4
     - K, 2 decimal places
   * - ``soil_level5_depth``
     - 
     - Depth below the land surface of soil level 5
     - m, 2 decimal places
   * - ``soil_level5_temperature``
     - 
     - Soil temperature at level 5
     - K, 2 decimal places
   * - ``soil_level6_depth``
     - 
     - Depth below the land surface of soil level 6
     - m, 2 decimal places
   * - ``soil_level6_temperature``
     - 
     - Soil temperature at level 6
     - K, 2 decimal places
   * - ``soil_level7_depth``
     - 
     - Depth below the land surface of soil level 7
     - m, 2 decimal places
   * - ``soil_level7_temperature``
     - 
     - Soil temperature at level 7
     - K, 2 decimal places
   * - ``soil_level8_depth``
     - 
     - Depth below the land surface of soil level 8
     - m, 2 decimal places
   * - ``soil_level8_temperature``
     - 
     - Soil temperature at level 8
     - K, 2 decimal places
   * - ``soil_level9_depth``
     - 
     - Depth below the land surface of soil level 9
     - m, 2 decimal places
   * - ``soil_level9_temperature``
     - 
     - Soil temperature at level 9
     - K, 2 decimal places
   * - ``soil_level10_depth``
     - 
     - Depth below the land surface of soil level 10
     - m, 2 decimal places
   * - ``soil_level10_temperature``
     - 
     - Soil temperature at level 10
     - K, 2 decimal places


Notes
-----

.. TODO: add usage notes, known limitations and change history.
