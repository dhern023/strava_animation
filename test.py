import argparse

parser = argparse.ArgumentParser(description = "Test program for debugging")
parser.add_argument('--name', '-n', required=True, type=str, help = "Please enter any string" )
parser.add_argument('--correct', '-c', action='store_true', help = "A boolean flag")
args = parser.parse_args()

def do_something(instance_args):
    if instance_args.correct:
        print(instance_args.name)

if __name__ == "__main__":
    do_something(args)