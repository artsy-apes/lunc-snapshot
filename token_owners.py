import csv
import json

import requests


def main():
    # Query token owners at the certain block height and write result to 'snapshot.csv'
    snapshot_block_height = "8361668"
    base_uri = "https://columbus-lcd.terra.dev/wasm/contracts/"
    artsyapes_contract = "terra1vdwz6zlrk6ptsxu97dk43uup9frchuwse8s6d8"
    query = {
        "owner_of": {
            "token_id": ""
        }
    }
    with open("snapshot.csv", 'w', encoding='utf-8') as f:
        csv_writer = csv.writer(f)
        for i in range(1, 5):
            query["owner_of"]["token_id"] = str(i)
            uri = f"{base_uri}/{artsyapes_contract}/store?" \
                  f"query_msg={json.dumps(query, ensure_ascii=False)}&" \
                  f"height={snapshot_block_height}"
            csv_writer.writerow([i, requests.get(uri).json()["result"]["owner"]])


if __name__ == '__main__':
    main()
