#!bin/bash

#Build the project
echo "Building the project"
python3.8 -m ip install -r requirements.txt

echo "Make Migrations.."
python3.8 manage.py makemigrations --noinput
python3.8 manage.py migrate --noinut

echo "collect Static .."
python3.8 manage.py collectstatic --noinut --clear