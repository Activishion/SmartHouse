D = docker
DC = docker compose
DC_file = docker-compose.production.yml
frontend = smarthouse-frontend
backend = smarthouse-backend
nginx = smarthouse-nginx

.PHONY: start
start:
	${DC} -f ${DC_file} up

.PHONY: update_application
update_application:	
	${D} rm backend nginx frontend
	${D} rmi ${frontend} ${backend} ${nginx}
	${DC} -f ${DC_file} up

.PHONY: delete_images
delete_images:
	${D} rmi ${frontend} ${backend} ${nginx}


# docker stop $(docker ps -aq)
# docker rm $(docker ps -aq)