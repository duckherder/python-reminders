"""How to get arguments from the command line."""

import sys
from argparse import ArgumentParser


if __name__ == "__main__":
    print("call this script using command line parameters, such as 'bob.txt --verbose=1'")
    print("len(sys.argv) =", len(sys.argv))
    print("type(sys.argv) =", type(sys.argv))
    print("sys.argv", sys.argv)
    if len(sys.argv) != 3:
        print("usage: <filename> [<switches>]")

    print("alternatively you can use ArgumentParser which give consistent interfaces and switch handling")
    parser = ArgumentParser(description="standard argument parser!")
    parser.add_argument('filename', type=str, nargs='+',        # positional argument - at least one filename required
                        help="input filename")
    parser.add_argument("-v", "--verbose",                      # optional arguments
                        type=int, default=0,
                        help="verbosity level")
    parser.add_argument("-H", "--extended-help", dest='extended',
                        default=False, action='store_true',
                        help="extended help")
    args = parser.parse_args()
    print("filename =", args.filename)
    print("verbosity level =", args.verbose)
    print("extended help =", args.extended)
