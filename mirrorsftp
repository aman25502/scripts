#!/bin/bash
echo "exit" | sshpass -p "$sf_pwd" ssh -tto StrictHostKeyChecking=no $sf_usr@shell.sourceforge.net create
rsync -v --rsh="sshpass -p $sf_pwd ssh -l $sf_usr" *.$EXT $sf_usr@shell.sourceforge.net:/home/frs/project/ahoy-builds
