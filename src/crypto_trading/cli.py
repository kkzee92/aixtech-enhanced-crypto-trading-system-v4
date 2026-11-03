"""CLI entry points for the paper-only trading information system."""

import argparse
from .demo import run_demo

def main():
    parser = argparse.ArgumentParser(description="AIxTech Crypto Trading Information System v4 (paper-only)")
    parser.add_argument("command", choices=["demo"], help="Command to run")
    args = parser.parse_args()
    if args.command == "demo":
        run_demo()

if __name__ == "__main__":
    main()
