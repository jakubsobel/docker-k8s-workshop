# Docker Exercise 2

## Result:
You will have a Docker image pushed to your Docker repository. Running that image will serve a simple HTML document on `localhost:8080` using `nginx`. You will be able to modify the files in real-time without the need to rebuild the image every time. 
## Steps:
1. Clone and checkout this branch on your machine.
2. Create a `Dockerfile`
3. Use [nginx](https://hub.docker.com/_/nginx) image 
4. Add lines responsible for copying the page from the `./src` directory to the specified directory inside the Docker image.
5. Add a line indicating the exposed port.
6. Build the image and run the container.
7. Run it again but with the `./src` folder mounted so you can edit the content in real time.
8. Push the image to your Docker repository

## Tips:
- Useful `Dockerfile` instructions:
  - `FROM <image>:<tag>`
  - `WORKDIR <path>`
  - `COPY <hostPath> <dockerPath>` - `dockerPath` is relative to the set `WORKDIR` 
  - `EXPOSE <port>`
  - [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- Useful `docker` commands:
  - `docker build -t <username>/<name>:<version> .`
  - `docker run [OPTIONS] <username>/<name>:<version> [COMMAND]`
    - `--rm` - automatically clean up the container and remove the file system when the container exits
    - `-d` - container will run in a detached (background) mode
    - `-p <hostPort>:<dockerPort>` - expose port
    - `-v <hostPath>:<dockerPath>` - mount filesystem; `dockerPath` is relative to the set `WORKDIR` 
  - `docker run <username>/<name>:<version>` 
  - `docker push <username>/<name>:<version>`    
  - [Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)
