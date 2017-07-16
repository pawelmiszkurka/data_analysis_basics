"""
Created on 16 Jul 2017
"""

from ftplib import FTP
import os

#define a funciton and assign 4 parameters with default values
def ftpDownloader(filename, host="ftp.pyclass.com", user="student@pyclass.com", passwd="student123"):
    #create ftp object instance for particular site
    ftp=FTP()
    ftp.login(user,passwd)
    print(ftp.nlst))
    ftp.cwd("Data")
    #prepare local working directory
    os.chdir("/Users/pawelmiszkurka/playground/data_analysis_basics/section_4")
    #create an empty file in working directory and assign file object to variable called file
    with open("isd-lite-format.pdf",'web') as file:
        #grab content of remote file using retrobinary method, content of a remote file will be written into local file
        ftp.retrbinary('RETR %s' % filename,file.write)
