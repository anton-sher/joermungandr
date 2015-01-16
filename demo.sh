#!/bin/sh

echo "1. Python."
rm joermungandr.rb
python3 joermungandr-init.py

echo "2. Ruby."
rm joermungandr.go
ruby joermungandr.rb

echo "3. Go"
rm joermungandr.groovy
go run joermungandr.go

echo "4. Groovy."
rm joermungandr.js
groovy joermungandr.groovy

echo "5. Node.js"
rm joermungandr.java
rm joermungandr*.class
node joermungandr.js

echo "6. Java"
rm joermungandr.c
rm joermungandr.cbin
javac joermungandr.java && java joermungandr

echo "7. C"
rm joermungandr.cpp
rm joermungandr.cppbin
gcc joermungandr.c -o joermungandr.cbin && ./joermungandr.cbin

echo "8. C++"
rm joermungandr.sh
g++ joermungandr.cpp -o joermungandr.cppbin && ./joermungandr.cppbin

echo "X. Bash."
rm joermungandr.py
bash joermungandr.sh

echo "Checking..."
diff -q joermungandr.py joermungandr-init.py
if [ $? == 0 ]; then
    echo "Joermungandr!"
else
    echo "Faen!"
fi