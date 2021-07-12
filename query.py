# Queries the NASA Exoplanet Archive's TAP API.

import urllib.request
import pyvo as vo

CLIENT_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP"

QUERY_URL = "https://exoplanetarchive.ipac.caltech.edu/TAP/sync?query="
COLUMNS = ["pl_name",
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

# Database to query. View databases at https://exoplanetarchive.ipac.caltech.edu/docs/TAP/usingTAP.html
QUERY_DB = "ps"
QUERY = "SELECT " + ",".join(COLUMNS) + " FROM " + QUERY_DB# + " WHERE " # need to add constraint
MANUAL_URL = QUERY_URL + QUERY + "&format=csv" # this needs to be encoded has spaces in it

def attemptNumber(val):
    """Attempts to turn value into number. Does PyVO do this already?"""
    newVal = val
    try:
        newVal = int(val)
    except:
        try:
            newVal = float(val)
        except:
            pass
    return newVal

def query_db():
    # print(QUERY_FORMATTER())
    # response = urllib.request.urlopen(QUERY_FORMATTER())

    print("RETRIEVING DATA")

    service = vo.dal.TAPService(CLIENT_URL)
    result = service.search(QUERY)

    print("DATA RETRIEVED")
    print("PROCESSING DATA")

    pl_list = []
    used_names = []
    for row in result:
        if row["pl_name"] in used_names:
            dict = pl_list[used_names.index(row["pl_name"])]
            for columnLabel in COLUMNS:
                val = row[columnLabel]
                if val:
                    dict[columnLabel] = val
        else:
            dict = {}
            for columnLabel in COLUMNS:
                val = row[columnLabel]
                if val:
                    dict[columnLabel] = val
            pl_list.append(dict)
            used_names.append(row["pl_name"])

    print("PROCESSED DATA")

    print("Entries:", len(pl_list))
    return pl_list