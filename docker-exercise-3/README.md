# Docker Exercise 3

## Result:
You will have a Docker image pushed to your Docker repository. Running that image will serve a simple API on `localhost:8081` using `python`. You will be able to modify the files in real-time without the need to rebuild the image every time. 
## Steps:
1. Clone and checkout this branch on your machine.
2. Create a `Dockerfile`
3. Use [python](https://hub.docker.com/_/python) image 
4. Run the image with an interactive terminal and play with some basic python commands.
5. To the `Dockerfile` add lines responsible for copying the server files from the `./src` directory to the specified directory inside the Docker image.
6. Add a line responsible for the python script dependencies installation.
7. Add a line responsible for starting the `app.py` script using a `python` binary.
8. Add a line indicating the exposed port.
9. Build the image and run the container.
10. Check `localhost:8081` and `localhost:8081/books`
11. Run it again but with the `./src` folder mounted so you can edit the content in real time.
12. Push the image to your Docker repository.

## Tips:
- Useful `Dockerfile` instructions:
  - `FROM <image>:<tag>`
  - `WORKDIR <path>`
  - `COPY <hostPath> <dockerPath>` - `dockerPath` is relative to the set `WORKDIR` 
  - `RUN ["executable", "param1", "param2"]`
  - `ENTRYPOINT ["executable", "param1", "param2"]`
  - `EXPOSE <port>`
  - [Dockerfile reference](https://docs.docker.com/engine/reference/builder/)
- Useful `docker` commands:
  - `docker build -t <username>/<name>:<version> .`
  - `docker run [OPTIONS] <username>/<name>:<version> [COMMAND]`
    - `--rm` - automatically clean up the container and remove the file system when the container exits
    - `-d` - container will run in a detached (background) mode
    - `-p <hostPort>:<dockerPort>` - expose port
    - `-v <hostPath>:<dockerPath>` - mount filesystem; `dockerPath` is relative to the set `WORKDIR` 
    - `-it` - interactive terminal
  - `docker run <username>/<name>:<version>` 
  - `docker push <username>/<name>:<version>`    
  - [Docker command line](https://docs.docker.com/engine/reference/commandline/cli/)
- Python script dependencies:
  - `pip install Flask`   
  - `pip install flask-cors`
