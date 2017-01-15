import ftplib


HOST = "ftp.mozilla.org"
DIRN = 'pub/mozilla.org/webtools'
FILE = 'bugzilla-LATEST.tar.gz'

def main():
    f = ftplib.FTP(HOST)
    F.login()
    f.cwd(DIRN)
    f.retrbinary("RETR {}".format(FILE),open(FILE,'wb').write())
    f.quit()
    
if __name__ == '__main__':
    main()    