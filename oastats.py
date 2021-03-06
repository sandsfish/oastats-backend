#!/usr/bin/env python

import os

os.environ.setdefault("OASTATS_SETTINGS", "pipeline.settings")

import fileinput
from pipeline.conf import settings
from pipeline.parse_log import parse
from pipeline.load_json import get_collection, insert
from pipeline.request import add_country, str_to_dt, req_to_url


collection = get_collection(settings.MONGO_DB,
                            settings.MONGO_COLLECTION,
                            settings.MONGO_CONNECTION)

def main():
    for line in fileinput.input():
        request = parse(line)
        if request is not None:
            request = str_to_dt(request)
            request = add_country(request)
            request = req_to_url(request)
            insert(collection, request)

if __name__ == '__main__':
    main()
