@echo off

docker build -t sqlite-crud-app .

docker run -d -p 5000:5000 --name sqlite-crud-running sqlite-crud-app

docker exec sqlite-crud-running python -m pytest test/test_create.py
docker exec sqlite-crud-running python -m pytest test/test_update.py
docker exec sqlite-crud-running python -m pytest test/test_delete.py

docker stop sqlite-crud-running
docker rm sqlite-crud-running

pause
