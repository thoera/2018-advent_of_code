#!/bin/bash

mkdir "day_$1"
cd "day_$1"
echo "# -*- coding: utf-8 -*-" > answer.py
echo -e "\n" >> answer.py
echo "# --- part one ---" >> answer.py
touch input.txt puzzle.txt
