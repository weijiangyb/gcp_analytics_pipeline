import json
import time
import datetime
from random import random
from google.auth import jwt
from google.cloud import pubsub_v1

import datetime
import logging
import sys
from typing import Any, Dict, List, Optional

import psycopg2.extras as p
import requests

#### TO DO
# CREDENTIALS_PATH = "PATH TO YOUR SERVICE ACCOUNT CREDENTIAL"
# PROJECT_ID = "YOUR PROJECT ID"
# TOPIC_ID = "YOUR PUB/SUB TOPIC ID"

# PubSub Utils Classes
class PubSubPublisher:
    def __init__(self, credentials_path, project_id, topic_id):
        credentials = jwt.Credentials.from_service_account_info(
            json.load(open(credentials_path)),
            audience="https://pubsub.googleapis.com/google.pubsub.v1.Publisher"
        )
        self.project_id = project_id
        self.topic_id = topic_id
        self.publisher = pubsub_v1.PublisherClient(credentials=credentials)
        self.topic_path = self.publisher.topic_path(self.project_id, self.topic_id)
    def publish(self, data: str):
        result = self.publisher.publish(self.topic_path, data.encode("utf-8"))
        return result
# Main publishing script
def main():
    i = 0
    publisher = PubSubPublisher(CREDENTIALS_PATH, PROJECT_ID, TOPIC_ID)

    def get_utc_from_unix_time(
        unix_ts: Optional[Any], second: int = 1000
    ) -> Optional[datetime.datetime]:
        return (
            datetime.datetime.utcfromtimestamp(int(unix_ts) / second)
            if unix_ts
            else None
        )

    def get_exchange_data() -> List[Dict[str, Any]]:
        url = 'https://api.coincap.io/v2/exchanges'
        try:
            r = requests.get(url)
        except requests.ConnectionError as ce:
            logging.error(f"There was an error with the request, {ce}")
            sys.exit(1)
        return r.json().get('data', [])

    exchanges = get_exchange_data()

    for data in exchanges:
        data['updated_dt'] = f"{get_utc_from_unix_time(data.get('updated'))}"
        data['time'] = f"{datetime.datetime.now()}"

        publisher.publish(json.dumps(data))
        time.sleep(random())

if __name__ == "__main__":
    main()
