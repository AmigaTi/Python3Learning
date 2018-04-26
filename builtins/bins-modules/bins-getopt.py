#!/usr/bin/python
# -*- coding: utf-8 -*-


import sys
import getopt


# getopt.getopt(args, shortopts, longopts=[])

# An example using only Unix style options
args = '-a -b -cfoo -d bar a1 a2'.split()
print(args)         # ['-a', '-b', '-cfoo', '-d', 'bar', 'a1', 'a2']

optlist, args = getopt.getopt(args, 'abc:d')
print(optlist)      # [('-a', ''), ('-b', ''), ('-c', 'foo'), ('-d', '')]
print(args)         # ['bar', 'a1', 'a2']


# Using long option names is equally easy
s = '--condition=foo --testing --output-file abc.def -x a1 a2'
args = s.split()
print(args)         # ['--condition=foo', '--testing', '--output=file', 'abc.def', '-x', 'a1', 'a2']

optlist, args = getopt.getopt(args, 'x', ['condition=', 'output-file=', 'testing'])
print(optlist)      # [('--condition', 'foo'), ('--testing', ''), ('--output-file', 'abc.def'), ('-x', '')]
print(args)         # ['a1', 'a2']
print('==' * 20)


# In a script, typical usage is something like this
def usage():
    print('''
Synopsis: 
    ./bin-getopt.py [option] [inapk] [outapk]
Option:
    -h, --help        get more information
    -p, --platform    specify a platform for signature, such as 8V9
    ''')


def main():
    shortopts = "hp:"
    longopts = ['help', 'platform=']
    try:
        opts, args = getopt.getopt(sys.argv[1:], shortopts, longopts)
    except getopt.GetoptError as err:
        # print help information and exit:
        print(err)      # will print something like "option -a not recognized"
        usage()
        sys.exit(2)
    print("opts = %s " % str(opts))
    print("args = %s " % str(args))
    platform = None
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            usage()
            sys.exit()
        elif opt in ("-p", "--platform"):
            platform = arg
        else:
            assert False, "unhandled option"

    inapk = None
    outapk = None
    if len(args) == 0:
        print("specify inapk or outapk")
        usage()
        sys.exit(2)
    elif len(args) == 1:
        inapk = args[0]
        outapk = args[0]
    elif len(args) == 2:
        inapk = args[0]
        outapk = args[1]

    print("platform = %s" % platform)
    print("inapk    = %s" % inapk)
    print("outapk   = %s" % outapk)


if __name__ == "__main__":
    main()


'''
D:\workspace\PycharmProjects\Basics>python .\builtins\bins-modules\bins-getopt.py -p 8V9 Settings.apk
opts = [('-p', '8V9')]
args = ['Settings.apk']
platform = 8V9
inapk    = Settings.apk
outapk   = Settings.apk


D:\workspace\PycharmProjects\Basics>python .\builtins\bins-modules\bins-getopt.py -p 8V9 Settings_unsigned.apk Settings_signed.apk
opts = [('-p', '8V9')]
args = ['Settings_unsigned.apk', 'Settings_signed.apk']
platform = 8V9
inapk    = Settings_unsigned.apk
outapk   = Settings_signed.apk


D:\workspace\PycharmProjects\Basics>python .\builtins\bins-modules\bins-getopt.py -h
opts = [('-h', '')]
args = []

Synopsis:
    ./bin-getopt.py [option] [inapk] [outapk]
Option:
    -h, --help        get more information
    -p, --platform    specify a platform for signature, such as 8V9
'''