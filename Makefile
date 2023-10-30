D = docker
DC = docker compose
DC_file = docker-compose.production.yml
frontend = smarthouse-frontend
backend = smarthouse-backend
nginx = smarthouse-nginx
admin = dpage/pgadmin4

.PHONY: start
start:
	${DC} -f ${DC_file} up

.PHONY: update_application
update_application:	
	${D} rm backend nginx frontend pg_admin
	${D} rmi ${frontend} ${backend} ${nginx} ${admin}
	${DC} -f ${DC_file} up

.PHONY: delete_images
delete_images:
	${D} rmi ${frontend} ${backend} ${nginx} ${admin}

.PHONY: enter_psql
enter_psql:
	${DC} -f ${DC_file} exec postresql psql --username=smarthouse_controler --dbname=postgres


# docker stop $(docker ps -aq)
# docker rm $(docker ps -aq)