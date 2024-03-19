import json

import requests


def threshold_query(
    min_longitude,
    max_longitude,
    min_latitude,
    max_latitude,
    start_year,
    end_year,
    height,
    filtering_thresholds,
    api_key,
):
    """
    Performs filtering operations on the Vestas Climate Library via the API query.

    Args:
      min_latitude (float): The minimum latitude of the area.
      max_latitude (float): The maximum latitude of the area.
      min_longitude (float): The minimum longitude of the area.
      max_longitude (float): The maximum longitude of the area.
      start_year (str): The start year (included) of the data in YYYY format.
      end_year (str): The end year (included) of the  data in YYYY format.
      height (float): The height (above surface) at which the data is analyzed.
      filtering_thresholds (dict): The filtering thresholds to apply to the data.
      api_key (str): The API key for accessing the Vestas Climate Library API.

    Returns:
      dict: The response from the API in JSON format.
    """
    api_url = "https://public-test.api.vestas.com/public/vestas-climate-library/v1/thresholdquery"
    headers = {"Content-Type": "application/json", "api_key": api_key}
    request = {
        "minxlat": min_latitude,
        "maxxlat": max_latitude,
        "minxlong": min_longitude,
        "maxxlong": max_longitude,
        "starttime": start_year,
        "endtime": end_year,
        "zHeights": [height, 40, 120],
        **filtering_thresholds,
    }

    response = requests.post(api_url, data=json.dumps(request), headers=headers)
    return response


# Example usage:
min_longitude = 10
max_longitude = 10.1
min_latitude = 45
max_latitude = 45.1
start_year = "2022"
end_year = "2023"
height = 155
# Define the filtering thresholds here.
# When both min and max values are defined, the proportion of data within the range will be calculated.
# When only min value is defined, the proportion of data greater than the min value will be calculated.
# When only max value is defined, the proportion of data less than the max value will be calculated.
filtering_thresholds = {
    "wsp_min": 4,
    "wsp_max": 16,  # Wind speed in m/s
    "tc_min": 0,
    "tc_max": 22,  # Temperature in Celsius
    "rho_min": 1.225,  # Air density in kg/m^3
    "ash_max": 0.33,  # Wind shear coefficient
    "icing_max": 0.5,  # Active icing, proportion of time
    "rh_min": 40,  # Relative humidity in percent
}

api_key = "insert-your-key"

response = threshold_query(
    min_longitude,
    max_longitude,
    min_latitude,
    max_latitude,
    start_year,
    end_year,
    height,
    filtering_thresholds,
    api_key,
)
print("Threshold Query: ")
print(response)
