#!/bin/sh

rm joermungandr.rb
python3 joermungandr-init.py

rm joermungandr.groovy
ruby joermungandr.rb

rm joermungandr.sh
groovy joermungandr.groovy

rm joermungandr.py
bash joermungandr.sh

diff -q joermungandr.py joermungandr-init.py
if [ $? == 0 ]; then
    echo "Joermungandr!"
else
    echo "Faen!"
fi