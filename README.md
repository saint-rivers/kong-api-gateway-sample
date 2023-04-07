# Kong API Gateway Demo

## Deploying Services with Docker Compose

```bash
docker compose up -d --build --scale user-api=3 --scale task-api=2
```

## Deploying Services with Docker Swarm

```bash
docker network network create --driver overlay my-network
docker stack deploy --compose-file swarm/docker-compose-kong.yml kong
docker stack deploy --compose-file swarm/docker-compose-flask.yml kong
```

```bash
docker stack rm kong
```
