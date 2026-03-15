from __future__ import annotations

import argparse
import json

from .models import load_model, available_models


def main() -> None:
    parser = argparse.ArgumentParser(prog='elegantcat')
    sub = parser.add_subparsers(dest='command', required=True)

    pred = sub.add_parser('predict')
    pred.add_argument('--model', choices=available_models(), required=True)
    pred.add_argument('--file', required=True)

    args = parser.parse_args()
    if args.command == 'predict':
        model = load_model(args.model)
        print(json.dumps(model.predict(args.file), indent=2))


if __name__ == '__main__':
    main()
