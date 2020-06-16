#!/bin/

import argparse
import json


def main():
    args = handle_args()
    topics = load_topics()

    if args.topic in topics:
        print(topics[args.topic])
    else:
        print("Unknown topic")


def handle_args():
    parser = argparse.ArgumentParser(description='PyDis help snippets')
    parser.prog = "pydis"
    parser.add_argument("-t", "--topic", dest="topic", action="store", help="Help topic", required=True)
    return parser.parse_args()


def load_topics():
    with open("topics.json") as f:
        return json.load(f)


if __name__ == "__main__":
    main()
