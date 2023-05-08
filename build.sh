#!bin/bash

#Build the project
echo "Building the project"
python3.9 -m ip install -r requirements.txt

echo "Make Migrations.."
python3.9 manage.py makemigrations --noinput
python3.9 manage.py migrate --noinut

echo "collect Static .."
python3.9 manage.py collectstatic --noinut --clear