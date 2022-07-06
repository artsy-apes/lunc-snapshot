import csv
import json
import sys

import requests


def main():
    """
    Query token owners at the certain block height and write result to 'snapshot.csv'
    """
    snapshot_block_height = "8000000"
    base_uri = "https://columbus-lcd.terra.dev/wasm/contracts/"
    artsyapes_contract = "terra1vdwz6zlrk6ptsxu97dk43uup9frchuwse8s6d8"
    num_of_tokens = 3777
    query = {
        "owner_of": {
            "token_id": ""
        }
    }
    with open("snapshot.csv", 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for i in range(1, num_of_tokens + 1):
            query["owner_of"]["token_id"] = str(i)
            uri = f"{base_uri}/{artsyapes_contract}/store?" \
                  f"query_msg={json.dumps(query, ensure_ascii=False)}&" \
                  f"height={snapshot_block_height}"
            csv_writer.writerow([i, requests.get(uri).json()["result"]["owner"]])

            # Print out counter
            sys.stdout.write("\r")
            sys.stdout.write(f"{i}/{num_of_tokens}")
            sys.stdout.flush()



if __name__ == '__main__':
    main()
