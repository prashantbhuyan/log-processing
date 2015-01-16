__author__ = 'Prashant B. Bhuyan'



import pandas as pd
import numpy as np
import scipy
import csv
import sys
import re
import time
import tkFileDialog as tkf


# def getFileName():

    # root = Tk()

    # root.withdraw()

    # return tkf.Open().show()



def preprocessFile(oldfile, newfile):

    try:

        with open(newfile,'w') as outfile, open(oldfile, 'r') as infile:


            for line in infile:
                line1 = re.sub(r"\[\d\d\:",r"    ",line)
                line2 = re.sub(r"\:\d\d\:\d\d\]", r"       ", line1)
                string1 = line2.replace("GET ", "GET")
                string2 = string1.replace("POST ", "POST")
                string3 = string2.replace(" HTTP/1.0", "HTTP")
                string4 = string3.replace("-","0")
                outfile.write(string4)

        return(outfile)






    except IOError:
        print "Error: File Not Found. . ."
        exit()

if __name__ == "__main__":

    oldfile = '/Users/MicrostrRes/Desktop/epadata.txt'
    newfile = '/Users/MicrostrRes/Desktop/nst_epadata.txt'



    preprocessFile(oldfile,newfile)

    data = pd.read_table(newfile, sep = '\s+')

    data.columns = ['Host', 'Timestamp', 'Request', 'Code', 'Bytes']

    # Problem 1 - Host that made most requests?
    print 'Problem 1 Solution: the host that made the most requests was sandy.rtptok1.epa.gov with 294 requests: \n', pd.value_counts(data['Host'])
    # Answer: The host that made the requests was 'sandy.rtptok1.epa.gov with 294 requests.

    # Problem 2 - Host that received the most Bytes
    # print data.sort('Bytes', ascending = False)
    # return the value of the most bytes
    print '\n', 'Problem 2 Solution: The value for the maximum bytes received by a host is', max(data['Bytes']), "bytes."
    # Answer: 4,816,896 bytes

    # Problem 3 - What was the busiest Server?

    sortedby_busiest_hour = data.groupby('Timestamp').count().sort('Request',ascending = False)
    sortedby_busiest_hour.columns = ['Requests','DuplicateData1','DuplicateData2','DuplicateData3']
    sortedby_busiest_hour.drop('DuplicateData1',1,inplace=True)
    sortedby_busiest_hour.drop('DuplicateData2',1,inplace=True)
    sortedby_busiest_hour.drop('DuplicateData3',1,inplace=True)

    print '\n','Problem 3 Solution: Server Load by Busiest Hours (Sorted by Most Requests By Hour): \n', sortedby_busiest_hour.stack()
    # Answer: The busiest server time was the 14th hour.

    # Problem 4 - what gif image was downloaded the most by requests.
    print '\n', 'Problem 4 Solution: Here is a list of the .GIF images sorted by most requests \n', pd.value_counts(data['Request'])
    # Answer: circle_logo_small_gif was downloaded the most with 3,189 requests.

    # Problem 5- return codes other than 200
    print '\n', 'Problem 5 Solution: Here are the instances of Codes other than 200 \n', pd.value_counts(data.Code[(data.Code!=200)])
    # Answer: Codes other than 200 include 304,302,404,501,403,500 and 400 with 304 having the most messages at 5,300.


























