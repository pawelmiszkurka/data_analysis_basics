from ftplib import FTP

ftp=FTP("ftp.pyclass.com")

ftp.login("student@pyclass.com","student123")

ftp.nlst()
# change working directory
ftp.cwd("Data")

