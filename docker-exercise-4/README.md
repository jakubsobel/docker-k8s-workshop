# Docker Exercise 4

## Result:
You will run both Excercise 2 and Excrercise 3 projects using `docker run` and then compare it to the Docker Compose approach of doing the same thing.
## Steps:

1. Using the knowledge from the previous exercises run `nginx` server and `python` API images, exposing the port and mounting the host directories.\
  You can optionally use my images: `jakubsobelyg/nginx-test:0.0.3` and `jakubsobelyg/python-test:0.0.4`
2. Check that `localhost:8080` is displaying the data from `localhost:8181/books`, kill both containers.
3. Clone and checkout this branch on your machine.
4. Open the unfinished `docker-compose.yaml` file.
5. Fill it with the values that you used for the `docker run` commands. Image, port and volumes.
6. Start the Docker Compose with single command and check that `localhost:8080` is displaying the data from `localhost:8181/books`

## Tips:
- Useful `docker-compose` fields:
  - ```yaml
    image: <username>/<name>:<version>
    volumes:
        - <hostPath>:<dockerPath>
        - ...
    ports:
        - <hostPort>:<dockerPort>
        - ...
    depends_on: <service_name>
    ```
  - [Docker Compose overview](https://docs.docker.com/compose/)

- Useful `docker` commands:
  - `docker run [OPTIONS] <username>/<name>:<version> [COMMAND]`
    - `--rm` - automatically clean up the container and remove the file system when the container exits
    - `-d` - container will run in a detached (background) mode
    - `-p <hostPort>:<dockerPort>` - expose port
    - `-v <hostPath>:<dockerPath>` - mount filesystem; `dockerPath` is relative to the set `WORKDIR` 
  - `docker compose up`   
  - [Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)
