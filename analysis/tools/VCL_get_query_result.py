import requests
import json

def get_query_result(query_id, api_key, records_per_page, page_number):
    """
    Get the paginated query result.

    Args:
        query_id (str): The ID of the query.
        api_key (str): The API key.
        records_per_page (int): The number of records per page.
        page_number (int): The page number to get.

    Returns:
        dict: The response JSON containing the query result.
    """
    api_url = f"https://public-test.api.vestas.com/public/vestas-climate-library/v1/queryresult/{query_id}/{records_per_page}/{page_number}"
    headers = {
        "Content-Type": "application/json",
        "api_key": api_key
    }
    response = requests.get(api_url, headers=headers)
    return response.json()

# Example usage
api_key = "insert-your-key"
query_id = "0f9de2dd-ebb1-4218-bf74-7166215e8225"
records_per_page = 500
page_number = 1

query_result = get_query_result(query_id, api_key, records_per_page, page_number)

print("Query Result: ")
print(query_result)
