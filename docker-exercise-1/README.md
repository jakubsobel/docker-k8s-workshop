# Docker Exercise 1

## Result:
You will have a Docker image pushed to your Docker repository. Running that image will ping `google.com`. It will be possible to change the URL as a container runtime parameter.
## Steps:
1. Create a `Dockerfile`
2. Use [alpine](https://hub.docker.com/_/alpine) image 
3. Add lines responsible for running the ping command
4. Build the image and run the container locally
5. Run the container locally with a different URL set as a runtime command
6. Push the image to your Docker repository
7. Remove it locally and try to run it again

## Tips:
- Useful `Dockerfile` instructions:
  - `FROM <image>:<tag>`
  - `ENTRYPOINT ["executable", "param1", "param2"]`
  - `CMD ["executable","param1","param2"]`
  - `CMD ["param1","param2"]`  - as default parameters to ENTRYPOINT
  - [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- Useful `docker` commands:
  - `docker build -t <username>/<name>:<version> .`
  - `docker run [OPTIONS] <username>/<name>:<version> [COMMAND]`
    - `--rm` - automatically clean up the container and remove the file system when the container exits
    - `-d` - container will run in a detached (background) mode
  - `docker run <username>/<name>:<version>` 
  - `docker push <username>/<name>:<version>`    
  - [Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)
