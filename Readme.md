# Pileta API

#### Building
```
API: docker build -t pileta-api
```

#### Runing
```
API: docker run -d -p 4000:80 pileta_api
DB: docker run -d -p 5432:3306 --name mysql_db -e MYSQL_ROOT_PASSWORD=root mysql:latest
```