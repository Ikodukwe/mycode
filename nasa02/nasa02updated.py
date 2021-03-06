#!/usr/bin/env python3

import requests ## 3rd party URL lookup

## define the main function
def main():
    neourl = 'https://api.nasa.gov/neo/rest/v1/feed?' # API URL
    startdate = 'start_date=2018-06-01'  ## start date for data
    enddate = '&end_date=END_DATE' ## create a mechanism to utilize enddate
    mykey = '&api_key=GUi3WOIHrksyfld4sz503GhgZlL0l9qymu4sMKTm' ## replace this with our API key

    neourl = neourl + startdate + mykey
    print(neourl)

    neojson = (requests.get(neourl)).json()

    print(neojson)
    print(neourl)

## call main
main()

