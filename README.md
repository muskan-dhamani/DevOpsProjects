Multi-Container App with Docker Compose

Steps:
1. docker-compose up --build
2. Go to "http://localhost:5000"
3. docker exec -it multi-container-app_db_1 psql -U user -d testdb
4. CREATE TABLE test_table (id SERIAL PRIMARY KEY, data TEXT);
INSERT INTO test_table (data) VALUES ('Hello from Docker Compose!');
5. Visit http://localhost:5000 again.
6. docker-compose down
