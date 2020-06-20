# Pileta API

#### System Requirements
 - Register, list and delete devices
 - Register measurements
 - Get last measurements

#### Instructions
1. Create the `docker-compose.yml` on root directory (use the .example)
2. Build the image by executing `sh entrypoint.sh build` 
3. Runn the app by executing `sh entrypoint.sh run`

#### About the entrypoint


TODO: 

- [DONE] Emprolijar carga de la app 
- [DONE] Ver tema alembic y migrations 
- Hacer capa de repositorio y agregarle la logica para softdelete
- Ver ModelBase (Cambiar nombre a BaseModel) si se puede hacer que el
  created_at y el updated_at te los tome por default
