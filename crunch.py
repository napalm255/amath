#!/usr/bin/env python
from __future__ import print_function
import amath
import boto3
import json
from datetime import datetime
from twilio.rest import TwilioRestClient

def send_sms(to, msg):
    try:
        cfg = json.load(open('twilio.cfg'))
        client = TwilioRestClient(cfg['account_sid'], cfg['auth_token'])
        for each t in cfg['to_numbers']:
            message = client.messages.create(to=cfg['to_numbers'], from_=cfg['from_number'], body=msg)
    except:
        return False

    return True

def add_perfect_number(number, start, end, runtime):
    db = boto3.resource('dynamodb')
    table = db.Table('perfect_numbers')
    try:
        response = table.put_item (
            Item = {
                       'number': str(number),
                       'start' : str(start),
                       'end' : str(end),
                       'runtime': str(runtime)
                   }
        )
    except:
        return False

    return True

def set_last_number(number, start, end, runtime):
    db = boto3.resource('dynamodb')
    table = db.Table('perfect_numbers_tracker')
    try:
        response = table.put_item (
            Item = {
                       'id': 'last_number',
                       'number': str(number),
                       'start': str(start),
                       'end' : str(end),
                       'runtime': str(runtime)
                   }
        )
    except:
        return False

    return True

def get_last_number():
    db = boto3.resource('dynamodb')
    table = db.Table('perfect_numbers_tracker')
    try:
        response = table.get_item(
            Key = { 'id': 'last_number' }
        )
    except:
        return False

    item = response['Item']
    return int(item['number'])


set_last_number(0, 0, 0, 0)
while True:
    n = get_last_number() + 1
    stime = datetime.now()
    r = amath.is_perfect(n)
    etime = datetime.now()
    runtime = etime - stime
    if r:
        add_perfect_number(n, stime, etime, runtime)
        print("%s is perfect." % n)
    set_last_number(n, stime, etime, runtime)
