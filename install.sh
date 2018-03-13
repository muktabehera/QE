#!/bin/bash
echo --- Setup virtual environment
virtualenv --python=python3.6 --always-copy .
echo --- Activate virtual environment
. ./bin/activate
echo --- Install dependencies
pip install --upgrade -r requirements.txt
echo --- Patch Libraries
# cp bravado-core-patch/* lib/python2.7/site-packages/bravado_core/ &> /dev/null
# cp bravado-core-patch/* lib/python3.5/site-packages/bravado_core/ &> /dev/null
cp bravado-core-patch/* lib/python3.6/site-packages/bravado_core/ &> /dev/null
echo --- Install complete
