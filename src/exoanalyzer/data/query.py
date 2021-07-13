"""Queries the NASA Exoplanet Archive's TAP API."""

import urllib.request
import pyvo as vo

_CLIENT_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP"
_DEFAULT_COLUMNS = ["pl_name",
    "hostname",
    "disc_year",
    "discoverymethod",
    "pl_orbper",
    "pl_orbsmax",
    "pl_orbeccen",
    "pl_rade",
    "pl_masse",
    "pl_bmasse",
    "pl_dens",
    "sy_dist",
    "st_metratio",
    # "pl_refname",
    # "st_refname",
    "dec"]
_DEFAULT_DB = "ps"

# Database to query. View databases at https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html
_QUERY_FORMAT = lambda columns, db: "SELECT " + ",".join(columns) + " FROM " + db# + " WHERE " # need to add constraint

def query(*query_columns, query_db):
    """Queries NASA Exoplanet TAP interface to retrieve data.
    Returns a list of dictionaries in format {column: data}
    and the DALResult from pyvo.
    """
    columns = query_columns or _DEFAULT_COLUMNS
    db = query_db or _DEFAULT_DB

    print("RETRIEVING DATA")

    service = vo.dal.TAPService(_CLIENT_URL)
    result = service.search(_QUERY_FORMAT(columns, db))

    print("DATA RETRIEVED")
    print("PROCESSING DATA")

    pl_list = []
    used_names = []
    for row in result:
        if row["pl_name"] in used_names:
            dict = pl_list[used_names.index(row["pl_name"])]
            for columnLabel in columns:
                val = row[columnLabel]
                if val:
                    dict[columnLabel] = val
        else:
            dict = {}
            for columnLabel in columns:
                val = row[columnLabel]
                if val:
                    dict[columnLabel] = val
            pl_list.append(dict)
            used_names.append(row["pl_name"])

    print("PROCESSED DATA")

    print("Exoplanet Entries:", len(pl_list))
    return pl_list, result