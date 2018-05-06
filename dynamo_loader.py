#!/usr/bin/python3

import boto3
import json
from decimal import Decimal

profile = 'dynamodb-local'
endpoint_url = 'http://localhost:8080'
table_name = 'Beers'

jsonfile = 'beers.json'

session = boto3.session.Session(profile_name=profile)
dynamo = session.resource('dynamodb', endpoint_url=endpoint_url)
table = dynamo.Table(table_name)

with table.batch_writer() as batch:
    with open(jsonfile, 'r') as f:
        for json_data in f:
            item = json.loads(json_data, parse_float=decimal.Decimal)
            batch.put_item(Item=item)
