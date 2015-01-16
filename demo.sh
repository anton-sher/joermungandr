#!/bin/sh

nr=1

echo "$nr. Python."
rm joermungandr.rb
python3 joermungandr-init.py
nr=$[nr + 1]

echo "$nr. Ruby."
rm joermungandr.go
ruby joermungandr.rb
nr=$[nr + 1]

echo "$nr. Go"
rm joermungandr.scala
go run joermungandr.go
nr=$[nr + 1]

echo "$nr. Scala"
rm joermungandr.groovy
scala joermungandr.scala
nr=$[nr + 1]

echo "$nr. Groovy."
rm joermungandr.js
groovy joermungandr.groovy
nr=$[nr + 1]

echo "$nr. Node.js"
rm joermungandr.java
rm joermungandr*.class
node joermungandr.js
nr=$[nr + 1]

echo "$nr. Java"
rm joermungandr.c
rm joermungandr.cbin
javac joermungandr.java && java joermungandr
nr=$[nr + 1]

echo "$nr. C"
rm joermungandr.cpp
rm joermungandr.cppbin
gcc joermungandr.c -o joermungandr.cbin && ./joermungandr.cbin
nr=$[nr + 1]

echo "$nr. C++"
rm joermungandr.sh
g++ joermungandr.cpp -o joermungandr.cppbin && ./joermungandr.cppbin
nr=$[nr + 1]

echo "$nr. Bash."
rm joermungandr.py
bash joermungandr.sh

echo "Checking..."
diff -q joermungandr.py joermungandr-init.py
if [ $? == 0 ]; then
    echo "Joermungandr!"
else
    echo "Faen!"
fi