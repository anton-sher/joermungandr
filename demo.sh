#!/bin/sh

echo "1. Python."
rm joermungandr.rb
python3 joermungandr-init.py

echo "2. Ruby."
rm joermungandr.groovy
ruby joermungandr.rb

echo "3. Groovy."
rm joermungandr.sh
groovy joermungandr.groovy

echo "4. Bash."
rm joermungandr.py
bash joermungandr.sh

echo "Checking..."
diff -q joermungandr.py joermungandr-init.py
if [ $? == 0 ]; then
    echo "Joermungandr!"
else
    echo "Faen!"
fi