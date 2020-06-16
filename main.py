#!/bin/

import argparse
import json

from fuzzywuzzy import process


def main():
    args = handle_args()
    topics = load_topics()

    # Get topic
    topic, score = process.extractOne(args.topic, topics.keys(), score_cutoff=75)

    if topic:
        print(topics[topic])
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
