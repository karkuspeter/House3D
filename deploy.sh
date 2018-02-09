#!/usr/bin/env bash

server=$1

if [ $# -lt 2 ]; then
        echo "only copying .py files for House3D"
        files='*.py'
        scp -r ./House3D/*.py ${server}:~/mclnet/House3D/House3D/
        scp -r ./tests/*.py ${server}:~/mclnet/House3D/House3D/
else
        files=$2
fi

scp ${files} ${server}:~/mclnet/House3D/