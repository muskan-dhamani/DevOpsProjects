Multi-Container App with Docker Compose

Steps:

docker-compose up --build
Go to "http://localhost:5000"
docker exec -it multi-container-app_db_1 psql -U user -d testdb
CREATE TABLE test_table (id SERIAL PRIMARY KEY, data TEXT); INSERT INTO test_table (data) VALUES ('Hello from Docker Compose!');
Visit http://localhost:5000 again.
docker-compose down