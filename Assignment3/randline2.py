#!/usr/bin/python

import sys
from optparse import OptionParser

class comm:
    def __init__(file1, file2):
         f1 = open(file1, 'r')
         f2 = open(file2, 'r')
         lines1 = f1.readlines()
         lines2 = f2.readlines()
         f1.close()
         f2.close()


def main():

   

"""    version_msg = "%prog 2.0"
    usage_msg = "%prog [OPTION]... FILE1 FILE2

Compare two files."



    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    parser.add_option("-n", "--numlines",#-short --long form
                      action="store", dest="numlines", default=1,
                      help="output NUMLINES lines (default 1)")
    parser.add_option("-u", "--unique",
                      action="store_true", dest="unique", default=False,
                      help="unique lines from files only")
    parser.add_option("-w", "--without-replacement",
                      action="store_true", dest="replacement", default=False,
                      help="output without replacement")
    parser.add_option("-1", action="store_true", dest="sup_1", default=False,
                      help="suppress column 1")
    options, args = parser.parse_args(sys.argv[1:]) #parse everything that is after the script name; -n 2: options filename: arguement: filename

    try:
        numlines = int(options.numlines)

    except:
        parser.error("invalid NUMLINES: {0}".
                     format(options.numlines))

    if numlines < 0:
        parser.error("negative count: {0}".
                     format(numlines))"""

    parser = OptionParser(version=version_msg,
                          usage=usage_msg)
    (options, args) = parser.parse_args(sys.argv[1:])
    
    if len(args) != 2:
        parser.error("wrong number of operands")
    input_file1 = args[0]
    input_file2 = args[1]

    try:
        generator = comm(input_file1, input_file2)
        sys.stdout.write(lines1)
        sys.stdout.write(lines2)

    except IOError as (errno, strerror): # Only captures IOError
        parser.error("I/O error({0}): {1}".
                     format(errno, strerror))

if __name__ == "__main__":
    main()

# l = [500, -1, 30]
# l.sort() //[-1, 30, 500]
# d = ()
# d["seas"] = 1234
# d["emergency"] = 911
# d["Tom] = 310888
# sorted(d.keys()) // sort keys
# l = d.keys()
# l.sort() // sort keys
# d.vaues()
# l = d.values()
# l.sort() // sort values
