CLIMAT
======

:Template: :template:`climat-template.json`
:Version: 1.1
:BUFR sequence: ``301150, 307073``
:Data category / sub-category: 0 / 20
:Header rows: 1 (column names in row 1)
:Sample data: :sample:`climat.csv`

CSV2BUFR template for the encoding of CLIMAT data.

Input CSV
---------

.. note::

   The CSV format described here is defined for this csv2bufr template only.
   It is not a WMO standard. The column names and layout are a convenience
   for preparing data for conversion; the standard is the BUFR sequence
   307073 defined in the *Manual on Codes* (WMO-No. 306), Volume I.2.

The regulations for encoding CLIMAT data in BUFR are given in B/C30,
*Regulations for reporting CLIMAT data in TDCF*, in the *Manual on Codes*
(WMO-No. 306), Volume I.2. References to them are given in brackets below.

The CSV holds the content of a CLIMAT report: monthly values for a land
station (sequence 307071) followed by the monthly normals (sequence 307072).
The **TAC** column gives the corresponding group in the traditional
alphanumeric CLIMAT code (FM 71), to help users converting from TAC. Note
that the units differ from TAC: values are given in SI units, not tenths of
hectopascals or degrees Celsius.

File format
^^^^^^^^^^^

* Comma separated (``,``), with no quoting of values.
* One header row containing the column names. Columns are matched by name,
  so their order does not matter, but every column listed below must be
  present.
* One row per station per month. Each row is encoded as a separate BUFR
  message.
* An empty cell is encoded as missing. Values that are not measured, not
  available or not known should be left empty.
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
   :widths: 30 12 38 20

   * - Column
     - TAC
     - Description
     - Units / values
   * - ``wigos_identifier_series``
     - 
     - WIGOS identifier series (first block of the WSI)
     - 0
   * - ``wigos_issuer_of_identifier``
     - 
     - WIGOS issuer of identifier (second block)
     - 0 - 65534
   * - ``wigos_issue_number``
     - 
     - WIGOS issue number (third block)
     - 0 - 65534
   * - ``wigos_local_identifier_character``
     - 
     - WIGOS local identifier (fourth block)
     - text, up to 16 characters
   * - ``block_number``
     - II
     - WMO block number. Must always be given (B/C30.2.1.1).
     - 0 - 99
   * - ``station_number``
     - iii
     - WMO station number. Must always be given (B/C30.2.1.1).
     - 0 - 999
   * - ``station_or_site_name``
     - 
     - Name of the station as published in WMO-No. 9, Volume A. If the name is longer than 20 characters, give a shortened version (B/C30.2.1.1).
     - text, up to 20 characters
   * - ``station_type``
     - 
     - Type of station (BUFR code table 0 02 001)
     - 0 = automatic, 1 = manned, 2 = hybrid (both manned and automatic)
   * - ``latitude``
     - 
     - Latitude of the station
     - degrees north, 5 decimal places
   * - ``longitude``
     - 
     - Longitude of the station
     - degrees east, 5 decimal places
   * - ``height_of_station``
     - 
     - Height of the station ground above mean sea level
     - m, 1 decimal place
   * - ``height_of_barometer``
     - 
     - Height of the barometer above mean sea level
     - m, 1 decimal place

Reporting period
^^^^^^^^^^^^^^^^

The year and month identify the month being reported. The template sets
the start of the month to day 1, 00:00, as required by B/C30.2.1.2, so the
day, hour and minute are not given in the CSV. A BUFR message must contain
reports for one month only (B/C30.2.2.1).

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - TAC
     - Description
     - Units / values
   * - ``year``
     - JJJ
     - Year of the month being reported
     - e.g. 2025
   * - ``month``
     - MM
     - Month being reported. Also used as the month of the normals in section 2.
     - 1 - 12
   * - ``time_zone_offset``
     - 
     - Displacement from 00 UTC on the first day of the month to the start of the period over which the monthly values (except precipitation) are calculated. For the recommended local-time month this is the difference between UTC and local time, UTC - LT: zero or negative east of Greenwich, zero or positive west of it (e.g. -1 for UTC+1, 3 for UTC-3) (B/C30.2.2.1). If national practice uses a different period, adjust the value accordingly (B/C30.4.2). Also applies to the normals.
     - hours, -13 to 13
   * - ``days_in_month``
     - 
     - Number of days in the month
     - days, 28 - 31

Monthly mean values (section 1)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - TAC
     - Description
     - Units / values
   * - ``mean_pressure``
     - P0P0P0P0
     - Monthly mean pressure at station level
     - Pa
   * - ``mean_pressure_sea_level``
     - PPPP
     - Monthly mean pressure reduced to mean sea level
     - Pa
   * - ``standard_pressure_level``
     - 
     - Standard pressure level for which ``geopotential_height`` is reported, for high-level stations that report geopotential instead of mean sea level pressure
     - Pa
   * - ``geopotential_height``
     - PPPP
     - Monthly mean geopotential height of the standard pressure level
     - gpm
   * - ``height_of_sensor``
     - 
     - Height of the temperature sensor above local ground
     - m, 2 decimal places
   * - ``air_temperature``
     - TTT
     - Monthly mean air temperature
     - K, 2 decimal places
   * - ``daily_mean_temp_deviation``
     - ststst
     - Standard deviation of daily mean values relative to the monthly mean air temperature
     - K, 2 decimal places
   * - ``method_for_extreme_temperatures``
     - iy
     - Type of reading used for the extreme temperatures (BUFR code table 0 02 051)
     - 1 = maximum/minimum thermometers, 2 = automated instruments, 3 = thermograph
   * - ``daily_read_time_max_temp``
     - GxGx
     - Principal time of daily reading of maximum temperature. This is the end of the 24-hour period to which the daily maximum temperature refers.
     - hour (UTC), 0 - 23
   * - ``max_temperature_last_24h``
     - TxTxTx
     - Mean daily maximum air temperature of the month
     - K, 2 decimal places
   * - ``daily_read_time_min_temp``
     - GnGn
     - Principal time of daily reading of minimum temperature. This is the end of the 24-hour period to which the daily minimum temperature refers.
     - hour (UTC), 0 - 23
   * - ``min_temperature_last_24h``
     - TnTnTn
     - Mean daily minimum air temperature of the month
     - K, 2 decimal places
   * - ``vapour_pressure``
     - eee
     - Mean vapour pressure for the month
     - Pa
   * - ``days_missing_pressure``
     - mPmP
     - Number of days missing from the records for pressure
     - days, 0 - 31
   * - ``days_missing_mean_temperature``
     - mTmT
     - Number of days missing from the records for air temperature
     - days, 0 - 31
   * - ``days_missing_vapour_pressure``
     - meme
     - Number of days missing from the records for vapour pressure
     - days, 0 - 31
   * - ``days_missing_max_temperature``
     - mTx
     - Number of days missing from the record for daily maximum air temperature
     - days, 0 - 31
   * - ``days_missing_min_temperature``
     - mTn
     - Number of days missing from the record for daily minimum air temperature
     - days, 0 - 31
   * - ``total_sunshine_hours``
     - S1S1S1
     - Total sunshine for the month
     - hours, 0 - 744
   * - ``total_sunshine_percent``
     - pspsps
     - Total sunshine duration as a percentage of the normal. If the percentage is greater than 0 but 1 % or less, give 1. If the normal is 0 hours, give 510. If the normal is not defined, leave empty (B/C30.2.3.1).
     - %
   * - ``days_missing_total_sunshine``
     - mSmS
     - Number of days missing from the records for sunshine
     - days, 0 - 31

Number of days of occurrence (sections 3 and 4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - TAC
     - Description
     - Units / values
   * - ``wind_over_10mps_days``
     - f10f10
     - Days with mean wind speed (10-minute) of 10 m s-1 (20 kt) or more
     - days, 0 - 31
   * - ``wind_over_20mps_days``
     - f20f20
     - Days with mean wind speed (10-minute) of 20 m s-1 (40 kt) or more
     - days, 0 - 31
   * - ``wind_over_30mps_days``
     - f30f30
     - Days with mean wind speed (10-minute) of 30 m s-1 (60 kt) or more
     - days, 0 - 31
   * - ``max_temp_below_zero_days``
     - Tx0Tx0
     - Days with maximum air temperature below 0 °C
     - days, 0 - 31
   * - ``max_temp_above_25_days``
     - T25T25
     - Days with maximum air temperature of 25 °C or more
     - days, 0 - 31
   * - ``max_temp_above_30_days``
     - T30T30
     - Days with maximum air temperature of 30 °C or more
     - days, 0 - 31
   * - ``max_temp_above_35_days``
     - T35T35
     - Days with maximum air temperature of 35 °C or more
     - days, 0 - 31
   * - ``max_temp_above_40_days``
     - T40T40
     - Days with maximum air temperature of 40 °C or more
     - days, 0 - 31
   * - ``min_temp_below_zero_days``
     - Tn0Tn0
     - Days with minimum air temperature below 0 °C
     - days, 0 - 31
   * - ``snow_over_0cm_days``
     - s00s00
     - Days with snow depth more than 0 cm
     - days, 0 - 31
   * - ``snow_over_1cm_days``
     - s01s01
     - Days with snow depth more than 1 cm
     - days, 0 - 31
   * - ``snow_over_10cm_days``
     - s10s10
     - Days with snow depth more than 10 cm
     - days, 0 - 31
   * - ``snow_over_50cm_days``
     - s50s50
     - Days with snow depth more than 50 cm
     - days, 0 - 31
   * - ``horizontal_visibility_below_50m_days``
     - V1V1
     - Days with visibility less than 50 m
     - days, 0 - 31
   * - ``horizontal_visibility_below_100m_days``
     - V2V2
     - Days with visibility less than 100 m
     - days, 0 - 31
   * - ``horizontal_visibility_below_1000m_days``
     - V3V3
     - Days with visibility less than 1000 m
     - days, 0 - 31
   * - ``hail_days``
     - DgrDgr
     - Days with hail
     - days, 0 - 31
   * - ``storm_days``
     - DtsDts
     - Days with thunderstorm(s)
     - days, 0 - 31

Extreme temperatures and wind (section 4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The ``*_qualifier`` columns show whether the extreme occurred on one day only
(0) or on more than one day in the month (1). If it occurred on more than one
day, give the first day in the ``*_day`` column. The same applies to the
highest daily precipitation.

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - TAC
     - Description
     - Units / values
   * - ``height_of_temp_sensor``
     - 
     - Height of the temperature sensor above local ground. Also used for the temperature normals.
     - m, 2 decimal places
   * - ``highest_daily_mean_temperature_qualifier``
     - 
     - Whether the highest daily mean temperature occurred on one day or more
     - 0 = on one day only, 1 = on more than one day (BUFR code table 0 08 053)
   * - ``highest_daily_mean_temperature_day``
     - yxyx
     - Day of the highest daily mean air temperature
     - 1 - 31
   * - ``highest_daily_mean_temperature``
     - TxdTxdTxd
     - Highest daily mean air temperature of the month
     - K, 2 decimal places
   * - ``lowest_daily_mean_temperature_qualifier``
     - 
     - Whether the lowest daily mean temperature occurred on one day or more
     - 0 = on one day only, 1 = on more than one day (BUFR code table 0 08 053)
   * - ``lowest_daily_mean_temperature_day``
     - ynyn
     - Day of the lowest daily mean air temperature
     - 1 - 31
   * - ``lowest_daily_mean_temperature``
     - TndTndTnd
     - Lowest daily mean air temperature of the month
     - K, 2 decimal places
   * - ``monthly_max_temperature_qualifier``
     - 
     - Whether the highest air temperature occurred on one day or more
     - 0 = on one day only, 1 = on more than one day (BUFR code table 0 08 053)
   * - ``monthly_max_temperature_day``
     - yaxyax
     - Day of the highest air temperature
     - 1 - 31
   * - ``monthly_max_temperature``
     - TaxTaxTax
     - Highest air temperature of the month
     - K, 2 decimal places
   * - ``monthly_min_temperature_qualifier``
     - 
     - Whether the lowest air temperature occurred on one day or more
     - 0 = on one day only, 1 = on more than one day (BUFR code table 0 08 053)
   * - ``monthly_min_temperature_day``
     - yanyan
     - Day of the lowest air temperature
     - 1 - 31
   * - ``monthly_min_temperature``
     - TanTanTan
     - Lowest air temperature of the month
     - K, 2 decimal places
   * - ``height_of_wind_sensor``
     - 
     - Height of the anemometer above local ground
     - m, 2 decimal places
   * - ``instrumentation_for_wind_measurement``
     - iw
     - Type of instrumentation for wind measurement (BUFR flag table 0 02 002). Add the values of the flags that apply: 8 = measured by certified instruments (0 = estimated using the Beaufort scale), 4 = originally measured in knots, 2 = originally measured in km h-1. If neither 4 nor 2 is set, the wind speed was originally measured in m s-1. For example, certified instruments measuring in knots = 12 (B/C30.2.5.7).
     - 0 - 15
   * - ``maximum_instantaneous_wind_speed_qualifier``
     - 
     - Whether the highest gust occurred on one day or more
     - 0 = on one day only, 1 = on more than one day (BUFR code table 0 08 053)
   * - ``maximum_instantaneous_wind_speed_day``
     - yfxyfx
     - Day of the highest gust
     - 1 - 31
   * - ``maximum_instantaneous_wind_speed``
     - fxfxfx
     - Highest gust (maximum instantaneous wind speed) of the month
     - m s-1

Precipitation (sections 1, 3 and 4)
^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^^

The monthly precipitation values cover the period from 06 UTC on the first
day of the month to 06 UTC on the first day of the following month
(B/C30.2.6.1). The template sets this period; it is not given in the CSV.

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - TAC
     - Description
     - Units / values
   * - ``height_of_rain_sensor``
     - 
     - Height of the precipitation gauge above local ground. Also used for the precipitation normals.
     - m, 2 decimal places
   * - ``total_accumulated_precipitation``
     - R1R1R1R1
     - Total precipitation for the month
     - kg m-2 (= mm), 1 decimal place; -0.1 = trace
   * - ``frequency_group_precipitation``
     - Rd
     - Frequency group of the monthly total within the 30-year reference period (BUFR code table 0 13 051). If the monthly total is zero, give the highest quintile that has 0.0 as its lower limit; for example, 5 if no rain fell in that month in any year of the 30-year period (B/C30.2.6.5).
     - 0 = below any value in the period, 1 - 5 = first to fifth quintile, 6 = above any value in the period
   * - ``days_with_precipitation_above_1mm``
     - nrnr
     - Days with precipitation of 1 mm or more
     - days, 0 - 31
   * - ``total_missing_days_with_respect_to_accumulation_or_average_precipitation``
     - mRmR
     - Number of days missing from the records for precipitation
     - days, 0 - 31
   * - ``rain_above_1kgpsm_days``
     - R01R01
     - Days with precipitation of 1.0 mm or more
     - days, 0 - 31
   * - ``rain_above_5kgpsm_days``
     - R05R05
     - Days with precipitation of 5.0 mm or more
     - days, 0 - 31
   * - ``rain_above_10kgpsm_days``
     - R10R10
     - Days with precipitation of 10.0 mm or more
     - days, 0 - 31
   * - ``rain_above_50kgpsm_days``
     - R50R50
     - Days with precipitation of 50.0 mm or more
     - days, 0 - 31
   * - ``rain_above_100kgpsm_days``
     - R100R100
     - Days with precipitation of 100.0 mm or more
     - days, 0 - 31
   * - ``rain_above_150kgpsm_days``
     - R150R150
     - Days with precipitation of 150.0 mm or more
     - days, 0 - 31
   * - ``highest_daily_amount_of_precipitation_qualifier``
     - 
     - Whether the highest daily precipitation occurred on one day or more
     - 0 = on one day only, 1 = on more than one day (BUFR code table 0 08 053)
   * - ``highest_daily_amount_of_precipitation_day``
     - yryr
     - Day of the highest daily precipitation
     - 1 - 31
   * - ``highest_daily_amount_of_precipitation``
     - RxRxRxRx
     - Highest daily amount of precipitation during the month
     - kg m-2 (= mm), 1 decimal place; -0.1 = trace

Monthly normals (section 2)
^^^^^^^^^^^^^^^^^^^^^^^^^^^

The normals are for the month given in ``month``. Precipitation normals have
their own reference period.

.. list-table::
   :header-rows: 1
   :widths: 30 12 38 20

   * - Column
     - TAC
     - Description
     - Units / values
   * - ``starting_reference_period_year``
     - YbYb
     - First year of the reference period for the normals (except precipitation)
     - e.g. 1991
   * - ``ending_reference_period_year``
     - YcYc
     - Last year of the reference period for the normals (except precipitation)
     - e.g. 2020
   * - ``normal_mean_pressure``
     - P0P0P0P0
     - Normal of monthly mean pressure at station level
     - Pa
   * - ``normal_mean_pressure_sea_level``
     - PPPP
     - Normal of monthly mean pressure reduced to mean sea level
     - Pa
   * - ``normal_standard_pressure_level``
     - 
     - Standard pressure level for which ``normal_geopotential_height_of_pressure_level`` is reported
     - Pa
   * - ``normal_geopotential_height_of_pressure_level``
     - PPPP
     - Normal of monthly mean geopotential height of the standard pressure level
     - gpm
   * - ``normal_air_temperature``
     - TTT
     - Normal of monthly mean air temperature
     - K, 2 decimal places
   * - ``normal_max_temperature_last_24h``
     - TxTxTx
     - Normal of mean daily maximum air temperature
     - K, 2 decimal places
   * - ``normal_min_temperature_last_24h``
     - TnTnTn
     - Normal of mean daily minimum air temperature
     - K, 2 decimal places
   * - ``normal_vapour_pressure``
     - eee
     - Normal of mean vapour pressure
     - Pa
   * - ``normal_daily_mean_temp_deviation``
     - ststst
     - Normal of the standard deviation of daily mean air temperature
     - K, 2 decimal places
   * - ``normal_total_sunshine``
     - S1S1S1
     - Normal of total sunshine for the month
     - hours
   * - ``rain_starting_reference_period_year``
     - 
     - First year of the reference period for the precipitation normals
     - e.g. 1991
   * - ``rain_ending_reference_period_year``
     - 
     - Last year of the reference period for the precipitation normals
     - e.g. 2020
   * - ``normal_total_accumulated_precipitation``
     - R1R1R1R1
     - Normal of total precipitation for the month
     - kg m-2 (= mm), 1 decimal place
   * - ``normal_days_with_precipitation_above_1mm``
     - nrnr
     - Normal of the number of days with precipitation of 1 mm or more
     - days
   * - ``normal_pressure_missing_years``
     - yPyP
     - Number of years missing from the calculation of the pressure normal
     - years, 0 - 30
   * - ``normal_temperature_missing_years``
     - yTyT
     - Number of years missing from the calculation of the mean air temperature normal
     - years, 0 - 30
   * - ``normal_extreme_temperature_missing_years``
     - yTxyTx
     - Number of years missing from the calculation of the mean extreme air temperature normal
     - years, 0 - 30
   * - ``normal_vapour_pressure_missing_years``
     - yeye
     - Number of years missing from the calculation of the vapour pressure normal
     - years, 0 - 30
   * - ``normal_rain_missing_years``
     - yRyR
     - Number of years missing from the calculation of the precipitation normal
     - years, 0 - 30
   * - ``normal_sunshine_duration_missing_years``
     - ySyS
     - Number of years missing from the calculation of the sunshine duration normal
     - years, 0 - 30
   * - ``normal_max_temperature_missing_years``
     - 
     - Number of years missing from the calculation of the maximum air temperature normal. Should be given, if available, in addition to ``normal_extreme_temperature_missing_years``.
     - years, 0 - 30
   * - ``normal_min_temperature_missing_years``
     - 
     - Number of years missing from the calculation of the minimum air temperature normal. Should be given, if available, in addition to ``normal_extreme_temperature_missing_years``.
     - years, 0 - 30


Notes
-----

.. TODO: add usage notes, known limitations and change history.
