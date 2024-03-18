import requests
import json
import os
from dotenv import load_dotenv

load_dotenv()

def get_query_status(query_id,api_key):
    """
    Get the status of a query.

    Args:
        api_key (str): The API key.
        query_id (str): The ID of the query.

    Returns:
        dict: The response JSON containing the query status.
    """
    api_url = f"https://public-test.api.vestas.com/public/vestas-climate-library/v1/querystatus/{query_id}"
    headers = {
        "Content-Type": "application/json",
        "api_key": api_key
    }
    response = requests.get(api_url, headers=headers)
    return response

# # Example usage

# api_key = os.environ["API_SECRET_KEY"]
# query_id = "0f9de2dd-ebb1-4218-bf74-7166215e8225"

# response = get_query_status(query_id, api_key)
# print("Query Status: ")
# print(response)
