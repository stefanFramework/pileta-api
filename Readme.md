# Pileta API

#### Building
```
API: sh pileta-api.sh build
```

#### Runing
```
API: sh pileta-api.sh start
DB: docker run -d -p 5432:3306 --name mysql_db -e MYSQL_ROOT_PASSWORD=root mysql:latest
```