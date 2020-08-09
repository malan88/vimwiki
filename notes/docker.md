- Access docker environment:
    - Use docker ps to get the name of the existing container
    - Use the command `docker exec -it <container name> /bin/bash` to get a bash
      shell in the container
    - Generically, use `docker exec -it <container name> <command>` to execute
      whatever command you specify in the container.
- You can refer to other containers within a `docker-compose.yml` by their service
  name (e.g., web, mariadb, etc) as the hostname. So you can refer to
  `root@mariadb` for a mysql URI
- To see the ip of a container: `sudo docker inspect -f '{{range
  .NetworkSettings.Networks}}{{.IPAddress}}{{end}}' <container name>`
- To remove an image (I mostly use for debugging purposes lol): `sudo docker rmi
  <imagename>`
- To rebuild a docker-compose image when we're adding pip requirements: `sudo
  docker-compose build --no-cache`
