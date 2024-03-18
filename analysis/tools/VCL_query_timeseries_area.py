import requests
import json

def timeseries_area_query(min_longitude, max_longitude, min_latitude, max_latitude, start_date, end_date, vars_4d, vars_3d, heights, api_key):
  """
  Queries the Vestas Climate Library API for timeseries data.

  Args:
    min_latitude (float): The minimum latitude of the area.
    max_latitude (float): The maximum latitude of the area.
    min_longitude (float): The minimum longitude of the area.
    max_longitude (float): The maximum longitude of the area.
    start_date (str): The start date of the timeseries data in YYYY-MM-DD format.
    end_date (str): The end date of the timeseries data in YYYY-MM-DD format.
    vars_4d (list): List of 4D variables to query.
    vars_3d (list): List of 3D variables to query.
    heights (list): List of heights above ground to query.
    api_key (str): The API key for accessing the Vestas Climate Library API.

  Returns:
    dict: The response from the API in JSON format.
  """
  api_url = "https://public-test.api.vestas.com/public/vestas-climate-library/v1/timeseriesareaquery"
  headers =  {
    "Content-Type":"application/json",
    "api_key": api_key
  }
  request = {
    "minxlat": min_latitude,
    "maxxlat": max_latitude,
    "minxlong": min_longitude,
    "maxxlong": max_longitude,
    "starttime": start_date,
    "endtime": end_date,
    "selectedVariables":{
        "3DVars":vars_3d,
        "4DVars":vars_4d, # Can be empty
        "zHeights":heights # Must not be empty if vars_4d is not empty
    }
  }
  response = requests.post(api_url, data=json.dumps(request), headers=headers)
  return response

# # Example usage:
# min_longitude = 10
# max_longitude = 10.1
# min_latitude = 45
# max_latitude = 45.1
# start_date = "20220101"
# end_date = "20220131"
# vars_4d = ["wsp","wdir","tk"] # Can be empty []
# vars_3d = ["swdown","t2"]
# heights = [80,240] # Must not be empty if vars_4d is not empty
# api_key = "insert-your-key"

# response = timeseries_area_query(min_longitude, max_longitude, min_latitude, max_latitude, start_date, end_date, vars_4d, vars_3d, heights, api_key)
# print("Timeseries Area Query: ")
# print(response)
