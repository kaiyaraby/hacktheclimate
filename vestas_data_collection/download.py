"""Command Line Tool to download the results of queries

Example usage:
`python download.py --csv-file "area_data.csv" --query-id "21e924a3-4dc6-4678-a71d-fadd7013f46f" --starting-page 1`
"""

import os
from argparse import ArgumentParser
from time import sleep

import pandas as pd
from dotenv import load_dotenv
from tools.VCL_get_query_result import get_query_result
from tqdm import tqdm

load_dotenv()
API_KEY = os.environ["API_SECRET_KEY"]


def process_result_to_file(csv_name, response_json, page_number):
    df = pd.DataFrame.from_records(response_json, index=range(len(response_json)))

    if page_number == 1:
        df.to_csv(csv_name, mode="a", index=False)
    else:
        df.to_csv(csv_name, mode="a", index=False, header=False)


def get_results_to_csv(api_key, query_id, csv_name, starting_page=1, attempts=3):
    records_per_page = 100000
    for i in tqdm(range(starting_page, starting_page + 20 + 1)):
        while attempts > 1:
            sleep(1)
            output = get_query_result(query_id, api_key, records_per_page, i)
            if output.status_code != 200:
                print(output.status_code)
                attempts -= 1
                print(output.content)
                if attempts >= 1:
                    output = get_query_result(query_id, api_key, records_per_page, i)
                else:
                    print(f"failed on page {i}")
                    return True
        response_json = output.json()

        process_result_to_file(csv_name, response_json, i)

        if len(response_json) != records_per_page:
            print("found the end!")
            print(f"page {i}: {len(response_json)}")
            return True
    return False


def main(args):
    if args.starting_page:
        starting_page = args.starting_page
    else:
        starting_page = 1

    count = 0
    while True:
        print(f"starting batch {count} ({starting_page + count*20}-{(starting_page + count*20)+20})")
        is_done = get_results_to_csv(API_KEY, args.query_id, args.csv_file, starting_page=(starting_page + count * 20))
        if is_done:
            break
        else:
            count += 1


def get_args():
    parser = ArgumentParser()
    parser.add_argument("--query-id", required=True)
    parser.add_argument("--csv-file", required=True)
    parser.add_argument("--starting-page", type=int)
    return parser.parse_args()


# Download area data query
# python download.py --csv-file "area_data.csv" --query-id "21e924a3-4dc6-4678-a71d-fadd7013f46f"

# Aggregation queries
# python download.py --csv-file "agg_data1.csv" --query-id "6a117fc4-030a-4584-8a3b-485d28f520ee"
# python download.py --csv-file "agg_data2.csv" --query-id "fee7d638-2254-412f-9cd0-60a9576c184a"
#
if __name__ == "__main__":
    args = get_args()
    main(args)
