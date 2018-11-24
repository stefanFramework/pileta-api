# Pileta API

#### Init
```
API: sh bootstrap.sh build
```

#### Runing
```
API: sh bootstrap.sh start
DB: docker run -d -p 5432:3306 --name mysql_db -e MYSQL_ROOT_PASSWORD=root mysql:latest
```