#!/usr/bin/python
import sys
import getopt
import time
import os
import dis
import socket
from datetime import date

if sys.version_info < (2, 6, 0) and sys.version_info > (3, 0, 0):
    sys.stderr.write("A minimium of Python 2.6.0 is required.  Python 3.0.0 has not been fully tested.")
    sys.exit(1)

class MethodCollector:
    def __init__(self):
        self = self
        self.optvars()
        self.main(sys.argv[1:])

    def printit(self):
        opts, args = getopt.getopt(sys.argv[1:], "c:i:o:h", ["cidr", "ip", "outputdir", "help"])
        print ("Running MethodCollector with " + str(sys.argv) + " on " + socket.gethostname() + " at " + time.strftime("%Y-%m-%d %H:%M:%S"))
        print "\tPress CTRL/C to cancel in ",
        for i in range(5):
            print str(5 - i) + " ",
            sys.stdout.flush()
            time.sleep(1)

    def optvars(self):
        global ipadress
        ipadress = ""
        global cidr
        cidr = ""
        global output
        output = ""
        global outputdir
        outputdir = ""
            
    def running(self):
        print("Scanning")
#################        dostuff()

    def usage(self):
        print "Usage: methodcollector.py [Options]"
        print "Ex: $  python methodcollector.py -c 10.10.0.0/16 -o /tmp/outputdir"
        print "\t  -c/--cidr: IP CIDR"
        print "\t  -i/--ip: Single IP"
        print "\t  -o/--outputdir <output dir>: Output Directory"
        print "\t  -h/--help: Help"
        
    def manpage(self):
        print "Usage: methodcollector.py [Options]"
        print "\t  -c/--cidr: IP CIDR"
        print "\t         This option will scan a cidr range (/24,/16,/8,/12...)"
        print "\t  -i/--ip: Single IP"
        print "\t         This option will single IP"
        print "\t  -o/--outputdir <output dir>: Output Directory"
        print "\t         This option specifies the output directory"
        print "\t  -h/--help: The standard smart alec response of \"You're Looking at it\""
        print "$  python methodcollector.py -c 10.10.0.0/16 -o /tmp/outputdir"
        
    def main(self,argv):
        sys.stderr.write("HTTP Methods Collector 0.1a" + "\t(https://github.com/Kvetch/)\n")
        sys.stderr.flush()
        try:
            opts, args = getopt.getopt(sys.argv[1:], "cio:h", ["cidr", "ip", "outputdir", "help"])
        except getopt.GetoptError as err:
            print(err)
            self.usage()
            sys.exit(2)
        
        # If there are no arguments print the help
        if len(sys.argv) == 1:
            self.usage()
            sys.exit()
        for opt, arg in opts:
            # If opt is help print the help
            if opt in ("-h", "--help"):
                self.manpage()
                sys.exit()
            elif opt in ('-c', "--cidr"):
                cidr = 1
            elif opt in ('-i', "--ip"):
                ipaddress = 1
            elif opt in ("-o", "--outputdir"):
                output = 1
                outputdir = str(arg)

#       if __name__ == "__main__":
#           main(sys.argv[1:])

x = MethodCollector()
x.printit()
x.running() 
            
