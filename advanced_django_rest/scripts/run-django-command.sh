#!/bin/bash

if [ $# -eq 0 ]; then
    echo "Usage: $0 <./run-django-commands.sh arguments>"
    exit 1
fi
echo $@
docker-compose run --rm app sh -c "python manage.py $@"

#./scripts/run-django-command.sh "wait_for_db && python manage.py migrate"