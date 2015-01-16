#!/bin/sh

rm joermungandr.rb
python3 joermungandr-init.py

rm joermungandr.groovy
ruby joermungandr.rb

rm joermungandr.py
groovy joermungandr.groovy

diff joermungandr.py joermungandr-init.py