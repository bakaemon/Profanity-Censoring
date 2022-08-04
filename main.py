# This is a sample Python script.
import argparse
from ProfanityChecker import ProfanityChecker

DESCRIPTION = "This is a simple tool to censor bad words. Support both Microsoft Document and plain text file."
if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=DESCRIPTION)
    # Add arguments here
    parser.add_argument("-i", "--Input")
    parser.add_argument("-c", "--Char", default="*")
    parser.add_argument("-o", "--Output")
    # read arguments
    args = parser.parse_args()
    if all(a is not None for a in [args.Input, args.Char, args.Output]):
        ProfanityChecker()\
            .load_badwords_from_file("data/badwords.txt")\
            .load_document(args.Input)\
            .censor(args.Char)\
            .export(args.Output)


# See PyCharm help at https://www.jetbrains.com/help/pycharm/
