import argparse

parser = argparse.ArgumentParser(description = "Test program for debugging")
parser.add_argument('--name', '-n', required=True, type=str, help = "Please enter any string" )
parser.add_argument('--correct', '-c', type=bool, default=False, help = "A boolean flag")
args = parser.parse_args()

if args.correct:
    print(args.name)