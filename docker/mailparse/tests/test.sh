#!/bin/bash
# This will quickly fire up Flask and do the python venv and run through the test cases on a local server on 5000

cd "$(dirname "$0")"
pwd
cd ..
export FLASK_APP=flaskr
export FLASK_ENV=development
rm -r venv
python3 -m venv venv
source venv/bin/activate
pip3 install flask
flask run &
sleep 5
cd tests/samples
for i in `ls`
do
curl -X POST --data-binary @$i http://127.0.0.1:80/post
done
pkill -9 -f  flask
