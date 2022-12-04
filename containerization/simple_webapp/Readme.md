# Instructions: working with docker

## Build docker image

```
docker build -t simple_webapp .
```

## Run docker container

```
docker run -p 80:80 --name simple_webapp simple_webapp
```

## Stop docker container

```
docker stop simple_webapp
```

## Remove docker container

```
docker rm simple_webapp
```

## Remove docker image

```
docker rmi simple_webapp
```