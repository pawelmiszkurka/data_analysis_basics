import os
from ftplib import FTP

def ftpDownloader(stationId,startYear,endYear,url="fpt.pyclass.com",user="student@pyclass.com",passwd="student123"):
    ftp=FTP(url)
    ftp.login(user,passwd)
    if not os.path.exists("/Users/pawelmiszkurka/playground/data_analysis_basics/section_4/in"):
        os.mkdirs("/Users/pawelmiszkurka/playground/data_analysis_basics/section_4/in")
    os.chdir("/Users/pawelmiszkurka/playground/data_analysis_basics/section_4/in")
    for year in range(startYear,endYear+1):
        fullpath='/Data/%s/%s-%s.gz' % (year,stationId,year)
        filename=os.path.basename(fullpath)
        try:
            with open(filename,'web') as file:
                ftp.retrbinary('RETR %S' % fullpath,file.write)
                print("% successfully downloaded" % filename)
        except error_perm:
            print("%s is not available" % filename)
            os.remove(filename)
    ftp.close()