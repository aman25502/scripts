# Copyright (C) 2020 Dhruv Gera
import glob
import sys
import subprocess
import select
import os
import pysftp
cnopts = pysftp.CnOpts()
cnopts.hostkeys = None

# Your particulars for accessing the sftp client
myHostname = "frs.sourceforge.net"
myUsername = os.environ['username']
myPassword = os.environ['password']

# Sourceforge or any other sftp client uploader script

with pysftp.Connection(host=myHostname, username=myUsername, password=myPassword, cnopts=cnopts) as sftp:
    print("Connection successful")

    # Switch to a remote directory
    sftp.cwd('/home/frs/project/ahoy-builds/gsi')  # Add your dir here
    # Obtain structure of the remote directory
    directory_structure = sftp.listdir_attr()

    source = 'output/$ZIP_NAME-GSI-Aonly.7z'  # The path where your file is stored on your drive
    # The path where you want to upload
    destination = '/home/frs/project/ahoy-builds/gsi/$ZIP_NAME-GSI-Aonly.7z'
    sftp.put(source, destination)

    source = 'output/$ZIP_NAME-GSI-AB.7z'  # The path where your file is stored on your drive
    # The path where you want to upload
    destination = '/home/frs/project/ahoy-builds/gsi/$ZIP_NAME-GSI-AB.7z'
    sftp.put(source, destination)
