#!/bin/bash
echo "exit" | sshpass -p "$sf_pwd" ssh -tto StrictHostKeyChecking=no $sf_usr@shell.sourceforge.net create
rsync -v --rsh="sshpass -p $sf_pwd ssh -l $sf_usr" output/$ZIP_NAME-GSI-Aonly.7z $sf_usr@shell.sourceforge.net:/home/frs/project/ahoy-builds/gsi
rsync -v --rsh="sshpass -p $sf_pwd ssh -l $sf_usr" output/$ZIP_NAME-GSI-AB.7z $sf_usr@shell.sourceforge.net:/home/frs/project/ahoy-builds/gsi
