#!/usr/bin/env python3
## Moving files with SFTP

## import paramiko so we can talk SSH
import paramiko
import os

## where to connect to
while True:
    ip_address = input("What is teh Ip address: ")
    user_name = input("Please provde username: ")
    pass_word = input("Password please: ")

    t = paramiko.Transport(ip_address, 22) ## IP and port

## how to connect (see other labs on using id_rsa private/public keypairs)
    t.connect(username=user_name, password=pass_word)

## Make an sftp connection object
    sftp = paramiko.SFTPClient.from_transport(t)

## iterate across the files within directory
    for x in os.listdir("/home/student/filestocopy/"): # iterate on directory contents
      if not os.path.isdir("/home/student/filestocopy/"+x): # filter everything that is NOT a directory
        sftp.put("/home/student/filestocopy/"+x, "/tmp/"+x) # move file to target location

## close the connection
    sftp.close() # close the connection

    contin = input("Do you wish to continue? Yes or No: ").upper()
    
    if contin == "NO":
      break


