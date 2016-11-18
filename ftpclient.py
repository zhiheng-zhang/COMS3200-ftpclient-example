from ftplib import FTP
import urllib.request


# Grab file from a ftp server
def grabftpfile():
    # Create new ftp socket
    try:
        ftp = FTP(website)
    except Exception:
        print ("Cannot reach the host name")
        return
    # Setting the username and password
    try:
        ftp.login(user='anonymous', passwd='coms3200@uq.edu.au')
    except Exception:
        print ("Cannot login with username and password")
        return
    # Setting cwd location
    try:
        ftp.cwd(cwd)
    except Exception:
        print ("Input cwd directory does not exist")
        return
    # Enable passive mode
    ftp.set_pasv(True)
    # Create new file named the same as file name in ftp server
    localfile = open(filename, 'wb')
    # Downloading the file into local machine
    try:
        ftp.retrbinary('RETR ' + filename, localfile.write, 1024)
    except Exception:
        print("Filename does no exist")
        return

    # Quit ftp connect
    ftp.quit()
    # Close the file
    localfile.close()

def grabHttpFile():
    url = website
    urllib.request.urlretrieve(url, filename)


"""Main function for type in different website, cwd and file name
 A client for downloading http file and ftp file, if using ftp client mode,
 the website will be like 'ftp.uq.edu.au', if using http client mode, the
 website will be like 'http://eait.uqstatic.net/up'"""

if __name__ == '__main__':
    # Input website name
    website = input("Write the website name\n")
    # Input file location
    cwd = input("Write the cwd location\n")
    # Input file name
    filename = input("Write the file name\n")
    # Run the grabFile() function
    selection = input("Ftp(1) or Http(2)?\n")
    if selection == '1':
        grabftpfile()
    elif selection == '2':
        grabHttpFile()




