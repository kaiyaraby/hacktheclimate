import requests
import json

def aggregation_query(min_longitude, max_longitude, min_latitude, max_latitude, start_date, end_date, aggregation, api_key):
  """
  Performs aggregation of the Vestas Climate Library data via the API query.

  Args:
    min_latitude (float): The minimum latitude of the area.
    max_latitude (float): The maximum latitude of the area.
    min_longitude (float): The minimum longitude of the area.
    max_longitude (float): The maximum longitude of the area.
    start_date (str): The start date of the timeseries data in YYYY-MM-DD format.
    end_date (str): The end date of the timeseries data in YYYY-MM-DD format.
    aggregation (dict): The aggregation functions and variables to be used in the query.
    api_key (str): The API key for accessing the Vestas Climate Library API.

  Returns:
    dict: The response from the API in JSON format.
  """
  api_url = "https://public-test.api.vestas.com/public/vestas-climate-library/v1/aggregationquery"
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
    "selectedFunction": aggregation
  }
  response = requests.post(api_url, data=json.dumps(request), headers=headers)
  return response.json()

def construct_aggregation_dict(agg_functions, vars_3d, vars_4d, heights):
  """
  Constructs the aggregation dictionary based on the provided arguments.

  Args:
    agg_functions (list): List of aggregation functions (AVG, MAX, MIN, SD).
    vars_3d (list): List of 3D variables.
    vars_4d (list): List of 4D variables.
    heights (list): List of heights.

  Returns:
    dict: The constructed aggregation dictionary.
  """
  aggregation_dict = {}
  for function in agg_functions:
    aggregation_dict[function] = {
      "4DVars": vars_4d,
      "3DVars": vars_3d,
      "zHeights": heights
    }
  return aggregation_dict

def construct_aggregation_dict_open(agg_functions, vars_3d_list, vars_4d_list, heights_list):
  """
  Constructs the aggregation dictionary based on the provided arguments.

  Args:
    agg_functions (list): List of aggregation functions (AVG, MAX, MIN, SD).
    vars_3d_list (list): List of lists containing 3D variables for each function.
    vars_4d_list (list): List of lists containing 4D variables for each function.
    heights_list (list): List of lists containing heights for each function.

  Returns:
    dict: The constructed aggregation dictionary.
  """
  aggregation_dict = {}
  for i, function in enumerate(agg_functions):
    aggregation_dict[function] = {
      "4DVars": vars_4d_list[i],
      "3DVars": vars_3d_list[i],
      "zHeights": heights_list[i]
    }
  return aggregation_dict


# Example usage:
min_longitude = 10
max_longitude = 10.1
min_latitude = 45
max_latitude = 45.1
start_date = "20220101"
end_date = "20220131"
agg_functions = ["AVG", "MAX"] #, "MIN", "SD"] # At least one function is required

# Here you can either use the construct_aggregation_dict (same variables and heights for all aggregation functions)
#                          or construct_aggregation_dict_open (different variables and heights for each aggregation function)
vars_3d = ["hgt", "t2"]
vars_4d = ["wsp", "tk"] # Can be empty
heights = [100, 200] # Must not be empty if 4D variables are used
#aggregation = construct_aggregation_dict(agg_functions, vars_3d, vars_4d, heights)

vars_3d_list = [["hgt", "t2"], ["swdown", "tc2"]]
vars_4d_list = [["wsp", "tk"], ["qvapor", "tc"]]
heights_list = [[100, 200], [80, 240]]
aggregation = construct_aggregation_dict_open(agg_functions, vars_3d_list, vars_4d_list, heights_list)

api_key = "insert-your-key"

response = aggregation_query(min_longitude, max_longitude, min_latitude, max_latitude, start_date, end_date, aggregation, api_key)
print("Aggregation Query: ")
print(response)
