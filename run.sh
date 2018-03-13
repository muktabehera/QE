#!/bin/bash
echo --- Activate virtual environment
. ./bin/activate
echo --- Collect and Run Tests
now=`date +"%Y%m%d_%H%M%S"`
python -m pytest --env data/qed_env.yml --auth data/pf_auth.yml --html=report/report-$now.html --junitxml=report/report-$now.xml --alluredir allure --disable-pytest-warnings --disable-warnings -v "$@"
exit $?
