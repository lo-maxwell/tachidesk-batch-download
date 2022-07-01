#port of shell script at tachidesk-batch-download.py
#dependencies:
#pip install requests
#tachidesk server running

import requests
import os
import sys
import argparse

def main(args):
    if (not args.port):
        args.port = 'http://127.0.0.1:4567'
    if (not args.id):
        sys.exit('Manga id not found. Use -h for list of parameters. Exiting program.')
    if (not args.start):
        args.start = 0
    if (not args.end):
        args.end = 999
        #arbitrary large value,
        #there's no problem if we go over the number of chapters
        #except that the server has more traffic than necessary
        #not sure if there's a way to query the maximum number of chapters in the manga
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/101.0.4951.67 Safari/537.36",
        "Accept": "application/json, text/plain, */*",
        "Accept-Language": "en-US,en;q=0.5",
        "Accept-Encoding": "gzip, deflate, br",
        "Connection": "keep-alive",
        "Referer": str(args.port) + "/manga/" + str(args.id),
        "Sec-Fetch-Dest": "empty",
        "Sec-Fetch-Mode": "cors",
        "Sec-Fetch-Site": "same-origin"
    }
    for i in range(args.start, args.end + 1):
        path = str(args.port) + '/api/v1/download/' + str(args.id) + '/chapter/' + str(i)
        response = requests.get(path, headers = headers)
        print('downloading chapter ' + str(i) + ': status code ' + str(response.status_code))

if __name__ == '__main__':
    parser = argparse.ArgumentParser(description='batch download from hosted tachidesk server')

    parser.add_argument('--port', dest='port', type=str, help='localhost path, default = http://127.0.0.1:4567')
    parser.add_argument('--id', dest='id', type=int, help='manga id to download from')
    parser.add_argument('--start', dest='start', type=int, help='first chapter to be downloaded, default = 0')
    parser.add_argument('--end', dest='end', type=int, help='last chapter to be downloaded (inclusive), default = 999')
    args = parser.parse_args()
    main(args)
