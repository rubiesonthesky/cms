#!/bin/bash
echo "Backing up current state"
current_time=$(date "+%d%m%Y_%H%M%S")
file_name='preupdate_state_'$current_time'.tar.gz'
tar -zcvf $file_name ./ &> /dev/null
echo "Pulling repository"
git pull
echo "Cleaning statics"
rm -rf ./static/
echo "Cleaning frontend"
cd frontend && gulp clean
echo "Building frontend"
npm install && bower install && gulp build
cd .. && source env/bin/activate
echo "Updating Python modules"
pip install -r requirements.txt
echo "Collecting statics"
python manage.py collectstatic --noinput
echo "Running migrations"
python manage.py migrate
deactivate
echo "Done"
