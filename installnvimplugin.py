#!/usr/bin/env python3
import argparse
import os

from Scripts.gui import main as start_gui
from Scripts.main import main as start_headless

def main():
    # creates a parser object to do the work
    parser = argparse.ArgumentParser()

    # add a mutally exclusive group (only one flag is allowed) to the parser
    group = parser.add_mutually_exclusive_group()

    # add a flag to it: "--gui"", which will be defined as boolean (store_true)
    group.add_argument("--gui", action="store_true",
                       help="Starts the gui")

    # parse the arguments which were passed in from cmmand line
    args = parser.parse_args()

    # we now look for the flag in the parser object and call the
    # respective "wrapper" function from one of the scipts (imports)
    if args.gui:
        start_gui()
    else:
        c_dir = os.getcwd()
        work_dir = os.path.join(c_dir, 'Scripts')
        start_headless(work_dir)

if __name__ == "__main__":
    main()