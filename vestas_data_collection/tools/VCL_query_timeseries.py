import json

import requests


def timeseries_query(latitude, longitude, start_date, end_date, vars_4d, vars_3d, heights, api_key):
    """
    Queries the Vestas Climate Library API for timeseries data.

    Args:
      latitude (float): The latitude of the location.
      longitude (float): The longitude of the location.
      start_date (str): The start date of the timeseries data in YYYY-MM-DD format.
      end_date (str): The end date of the timeseries data in YYYY-MM-DD format.
      vars_4d (list): List of 4D variables to query.
      vars_3d (list): List of 3D variables to query.
      heights (list): List of heights to query.
      api_key (str): The API key for accessing the Vestas Climate Library API.

    Returns:
      dict: The response from the API in JSON format.
    """
    api_url = "https://public-test.api.vestas.com/public/vestas-climate-library/v1/timeseriesquery"
    headers = {"Content-Type": "application/json", "api_key": api_key}
    request = {
        "latitude": latitude,
        "longitude": longitude,
        "startDate": start_date,
        "endDate": end_date,
        "vars4D": vars_4d,  # Can be empty
        "vars3D": vars_3d,
        "heights": heights,  # Must not be empty if vars_4d is not empty
    }
    response = requests.post(api_url, data=json.dumps(request), headers=headers)
    return response


# # Example usage:
# latitude = 45
# longitude = 10
# start_date = "2010-01-01"
# end_date = "2024-01-30"
# vars_4d = ["wsp","wdir"]
# vars_3d = ["swdown","t2"]
# heights = [80,240]
# api_key = "insert-your-key"

# response = timeseries_query(latitude, longitude, start_date, end_date, vars_4d, vars_3d, heights, api_key)
# print("Timeseries Query: ")
# print(response)
