"""Score an incident from impact (1-5) and urgency (1-5) into P1-P4.

Usage: python3 main.py --impact 4 --urgency 5
"""
import argparse
import sys


def score(impact, urgency):
    total = impact + urgency
    if total >= 9:
        return "P1"
    if total >= 7:
        return "P2"
    if total >= 5:
        return "P3"
    return "P4"


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--impact", type=int, required=True, choices=range(1, 6))
    parser.add_argument("--urgency", type=int, required=True, choices=range(1, 6))
    args = parser.parse_args(argv)
    print(f"Impact {args.impact} + Urgency {args.urgency} = {args.impact + args.urgency} -> {score(args.impact, args.urgency)}")
    return 0


if __name__ == "__main__":
    sys.exit(main())
