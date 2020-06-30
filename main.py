#!/bin/

import argparse
import json

from fuzzywuzzy import process


def main():
    args = handle_args()
    topics = load_topics()

    # Get topic
    matches = process.extractBests(args.topic, topics.keys(), score_cutoff=60)

    for topic, score in matches:
        if topic:
            print(f"{topic:20} - {score} - {topics[topic]}")
        else:
            print("Unknown topic")


def handle_args():
    parser = argparse.ArgumentParser(description='PyDis help snippets')
    parser.prog = "pydis"
    parser.add_argument("topic", action="store", help="Help topic")
    return parser.parse_args()


def load_topics():
    with open("topics.json") as f:
        return json.load(f)


if __name__ == "__main__":
    main()
