#! /bin/bash
grep 1809102021 01.csv
if [ $? == 0 ];
then
    echo 'find'
fi

