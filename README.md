## csv2bufr-templates

Repository for csv2bufr templates

> **Note:** The templates in this repository are example templates provided to assist with encoding observational data to BUFR format using [csv2bufr](https://github.com/wmo-im/csv2bufr). They are **not** official WMO data formats or standards. Users are responsible for ensuring that any encoded data meets the requirements of the intended data exchange or submission.

## Documentation

Documentation is in [`docs/`](docs/) and is built with Sphinx for Read the Docs. To build it locally:

```bash
pip install -r docs/requirements.txt
cd docs && make html
```

See the [csv2bufr documentation](https://csv2bufr.readthedocs.io) for details of the template format and how to use csv2bufr.

## Contents

1. aws-template.json: Template for simplified CSV data from automatic weather stations.
1. daycli-template.json: Template for daily climate data (DAYCLI version 2, BUFR sequence 307075).
1. daycli-v3.json: Template for daily climate data (DAYCLI version 3, BUFR sequence 307095).
1. CampbellAfrica-v1-template.json: Template for CSV data from Campbell AWS stations deployed in Africa.
1. climat-template.json: Template for monthly climate data.
1. Climsoft-hourly.json: Template for CSV output from Climsoft data management system.
1. Surface-RA-IV-100.json: Template for surface land station data using the RA-IV BUFR sequence (BUFR sequence 301150, 307080).
